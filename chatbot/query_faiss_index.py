import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import os

CHUNKS_FILE = "chunks.json"
INDEX_FILE = "faiss_index.bin"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_chunks(path):
    with open(path, "r", encoding="utf-8") as fp:
        return json.load(fp)

def normalize(vec):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return vec / norm

if __name__ == "__main__":
    if not os.path.exists(CHUNKS_FILE) or not os.path.exists(INDEX_FILE):
        raise SystemExit("make sure chunks.json and faiss_index.bin are available in this folder")


    print("Loading model(small)...")
    model  = SentenceTransformer(MODEL_NAME)


    print("Loading FAISS index....")
    index = faiss.read_index(INDEX_FILE)

    chunks = load_chunks(CHUNKS_FILE)
    print(f"Loaded {len(chunks)} chunks and index with {index.ntotal} vectors")


    while True:
        query = input("\nAsk a question(enter quit to exit)...").strip()
        if not query:
            continue
        if query.lower() in ("exit", "quit"):
            break

        q_vec = model.encode([query], convert_to_numpy=True)[0].astype("float32")
        q_vec = normalize(q_vec)
        q_vec = q_vec.reshape(1,-1)

        k = 3
        distances, indices = index.search(q_vec, k)


        for rank, idx in enumerate(indices[0]):
            if idx < 0:
                continue
            score = distances[0][rank]
            print(f"\n----result  {rank+1} (idx ={idx}, score={score:.4f}----")
            print(chunks[idx][:800].replace("\n", " ").strip() + "....")
