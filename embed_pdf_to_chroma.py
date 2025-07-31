import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb

# Load environment variables
load_dotenv()

# Setup ChromaDB client (creates .chroma/ folder in your project)
chroma_client = chromadb.PersistentClient(path="./chroma_store")


collection_name = "pdf_chunks"
if collection_name in chroma_client.list_collections():
    chroma_client.delete_collection(name=collection_name)

collection = chroma_client.create_collection(name=collection_name)

# 1. Read PDF and split into chunks
def read_pdf(file_path):
    doc = fitz.open(file_path)
    chunks = []
    for page in doc:
        text = page.get_text()
        chunks.extend([text[i:i+500] for i in range(0, len(text), 500)])
    return chunks

# 2. Generate embeddings
def generate_embeddings(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    vectors = model.encode(chunks)
    return vectors

# 3. Store chunks in ChromaDB
def store_in_chroma(chunks, vectors):
    collection.add(
        documents=chunks,
        embeddings=[vec.tolist() for vec in vectors],
        ids=[f"chunk-{i}" for i in range(len(chunks))]
    )
    print(f"✅ Stored {len(chunks)} chunks in ChromaDB.")

if __name__ == "__main__":
    pdf_path = "F16.pdf"  # Place your PDF in the same folder
    chunks = read_pdf(pdf_path)
    print(f"🔍 Read {len(chunks)} chunks from PDF.")
    vectors = generate_embeddings(chunks)
    store_in_chroma(chunks, vectors)
