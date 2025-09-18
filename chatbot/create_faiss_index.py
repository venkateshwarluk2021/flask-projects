import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from tqdm import tqdm
import os

CHUNKS_FILE = "chunks.json"
INDEX_FILE = "faiss_index.bin"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_chunks(path):
    with open(path, "r", encoding="utf-8") as fp:
        return json.load(fp)



def compute_embeddings(chunks, model, batch_size=32):
    embeddings = []
    for i in tqdm(range(0, len(chunks), batch_size),desc="Embedding batches"):
        batch = chunks[i:i+batch_size]
        emb = model.encode(batch, convert_to_numpy=True, show_progress_bar=False)
        embeddings.append(emb)
    embeddings = np.vstack(embeddings)
    return embeddings

def normalize_embeddings(emb):
    norms = np.linalg.norm(emb, axis=1, keepdims=True)
    norms[norms==0] = 1e-9
    return emb / norms

if __name__ == "__main__":
    if not os.path.exists(CHUNKS_FILE):
        raise SystemExit(f"put {CHUNKS_FILE} in this folder before running.")
    print("Loading chunks....")
    chunks = load_chunks(CHUNKS_FILE)
    print(f"Loaded {len(chunks)} chunks")

    print("Load model (this will download on first run...)")
    model = SentenceTransformer(MODEL_NAME)

    print("computing embeddings")
    embeddings = compute_embeddings(chunks, model, batch_size=32)


    print("normalising embeddings for cosine similarity...")
    embeddings = normalize_embeddings(embeddings).astype("float32")

    dim = embeddings.shape[1]
    print(f"Embeddings dimensions {dim}")

    print("creating FAISS index (IndexFlatIP for cosine similarity with normalize vectors...)")
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    print(f"Index contains {index.ntotal} vectors")


    print(f"saving index to {INDEX_FILE}...")
    faiss.write_index(index, INDEX_FILE)

    print("Done. saved faiss_index.bin  and keep chunks.json as metadata")
    
