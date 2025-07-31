import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
gemini = genai.GenerativeModel(model_name="gemini-2.0-flash")


embed_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="./chroma_store")

collection = chroma_client.get_collection(name="pdf_chunks")

user_question = input("Ask your question: ")

user_vector = embed_model.encode([user_question])[0]

results = collection.query(
    query_embeddings=[user_vector.tolist()],
    n_results=3
)


top_chunks = results['documents'][0]
context_text = "\n---\n".join(top_chunks)


final_prompt = f"""
You are a helpful assistant. Use the following context to answer the question.
If context is not relevant, say "I don't know from the document".

Context:
{context_text}

Question:
{user_question}
"""

response = gemini.generate_content(final_prompt)
print("\n🤖 Gemini says:\n")
print(response.text)
