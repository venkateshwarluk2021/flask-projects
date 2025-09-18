from pypdf import PdfReader
import re
import json


# for extracting text from pdf
def extract_clean_text(pdf_path):
    reader = PdfReader(pdf_path)

    all_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n"

    clean_text = re.sub(r'\s+',' ', all_text).strip()


    return clean_text


# for converting text into chunks of small size
def chunk_text(text, chunk_size=500, overlap=50):
    """
    splits text into overlapping chunks
    chunk_size=maximum characters per chunk
    overlap= repeated chars from previous chunk
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start+chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

# implementing searching using function
def search_chunks(chunks, query, top_n=2):
    """
    simple keyword search across chunks
    returns top_n most relevent chunks
    """
    query_words = query.lower().split()
    scored = []

    for idx, chunk in enumerate(chunks):
        score = sum(chunk.lower().count(word) for word in query_words)
        if score > 0:
            scored.append((score, idx ,chunk))

    scored.sort(reverse=True, key=lambda x:x[0])
    return scored[:top_n]


    
if __name__ == "__main__":
    text = extract_clean_text("sample.pdf")
##    print(text[:1000])
    chunks = chunk_text(text, chunk_size=500, overlap=50)
    with open("chunks.json", "w", encoding="utf-8") as fp:
        json.dump(chunks, fp, ensure_ascii=False, indent=2)
    
##    print("length of chunks: ", len(chunks))
##    print("\n\nfirst chunk:\n\n ", chunks[0])
##    print("\n\nLast chunk: \n\n", chunks[-1])
##    while True:
##        query = input("\nAsk A question (enter quit): \n")
##        if query.lower() == "quit":
##            break
##
##        search_results = search_chunks(chunks, query)
##        if not search_results:
##            print("\n\nInvalid keyword .could not find any matching results\n\n")
##        else:
##            for score, idx, chunk in search_results:
##                print(f"\n\n Chunck {idx} (score: {score}) : \n {chunk[:300]}........")
##
