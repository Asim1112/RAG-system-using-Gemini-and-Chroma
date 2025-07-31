# 🤖 RAG system using Gemini and Chroma

This project is a simple and powerful Retrieval-Augmented Generation (RAG) system that uses Google's **Gemini AI model** and **ChromaDB** to answer questions from any PDF document.

> Upload a PDF → Embed it → Ask any question → Get intelligent answers with context!

---

## 🚀 Features

- ✅ Upload any PDF and convert its content into vector embeddings
- ✅ Store and search embeddings using **ChromaDB**
- ✅ Use **Google Gemini (2.0 Flash)** for context-aware answer generation
- ✅ Fast and accurate chunk-based querying
- ✅ Modular and clean Python codebase

---

## 🧠 How It Works

1. **Embedding PDF to Chroma**  
   `embed_pdf_to_chroma.py`  
   - Loads PDF
   - Splits it into chunks
   - Converts chunks to embeddings using `sentence-transformers`
   - Stores them in a Chroma collection

2. **Asking Questions (RAG)**  
   `query_gemini_with_rag.py`  
   - Takes user input (your question)
   - Embeds the question
   - Finds top matching chunks from ChromaDB
   - Sends those as context to Gemini API
   - Gemini returns a smart, context-rich response

---

## 📂 Project Structure


RAG system using Gemini and Chroma/
│
├── embed_pdf_to_chroma.py # Step 1: Upload and embed PDF
├── query_gemini_with_rag.py # Step 2: Ask questions via Gemini + Chroma
├── requirements.txt # Dependencies
├── .gitignore # Ignored files (e.g., .env, .venv, chroma_store)
├── README.md # You're reading it!
├── .env # Your Gemini API key (keep it secret!)
├── chroma_store/ # Persistent Chroma vector store
├── F16.pdf # Example/test PDF (ignored in git)
├── .venv/ # Python virtual environment (ignored)
└── uv.lock / .python-version # Optional Python env files



---

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/Asim1112/RAG-system-using-Gemini-and-Chroma.git
   cd gemini-rag-pdf


2. **Install dependencies**

pip install -r requirements.txt

3. **Add your Gemini API key**

GEMINI_API_KEY=your-gemini-api-key-here

4. **Run the embed script**

python embed_pdf_to_chroma.py

5. **Ask questions!**


🙋‍♂️ Author
Asim Hussain
🖥️ Web Developer | 👨‍💻 Python & AI Learner | 🚀 GIAIC Elite Student
📍 Karachi, Pakistan
📫 Connect on LinkedIn "https://linkedin.com/in/asim-hussain-5429252b8"

