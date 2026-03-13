# RAG-based YouTube Video QA & Summarization System

A Retrieval-Augmented Generation (RAG) application that converts YouTube video transcripts into a searchable knowledge base.
The system allows users to ask questions or generate summaries from video content using semantic retrieval and LLMs.

---

## 🚀 Features

* Extracts **YouTube video transcripts automatically**
* Converts transcripts into **semantic chunks**
* Generates **vector embeddings using OpenAI**
* Stores vectors in a **FAISS vector database**
* Uses **Retrieval-Augmented Generation (RAG)** for context-grounded answers
* Supports **question answering and video summarization**

---

## 🏗 System Architecture

User Query
↓
Retriever (FAISS similarity search)
↓
Relevant Transcript Chunks
↓
Prompt Template
↓
LLM (GPT-4o-mini)
↓
Final Answer / Summary

---

## ⚙️ Tech Stack

* **Python**
* **LangChain**
* **OpenAI API (GPT-4o-mini, text-embedding-3-small)**
* **FAISS Vector Database**
* **YouTube Transcript API**
* **Retrieval-Augmented Generation (RAG)**

---

## 📂 Project Structure

```
youtube-rag-system/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠 Installation

Clone the repository

```
git clone https://github.com/yourusername/youtube-rag-system.git
cd youtube-rag-system
```

Install dependencies

```
pip install -r requirements.txt
```

Add your OpenAI API key to `.env`

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

Run the script:

```
python app.py
```

Example query:

```
can you summarize the video
```

---

## 📌 Example Use Cases

* Summarizing long educational videos
* Asking questions about lecture content
* Extracting key insights from technical talks
* Building searchable video knowledge bases

---

## 📈 Future Improvements

* Support **any YouTube URL input**
* Add **Streamlit UI for interactive chat**
* Implement **persistent vector database**
* Add **conversation memory**

---

## 👤 Author

**Bhoopender Baghel**

AI / GenAI Projects

