# RAG-based YouTube Video QA & Summarization System

A Retrieval-Augmented Generation (RAG) application that converts YouTube video transcripts into a searchable knowledge base.
The system allows users to ask questions, generate summaries, and have **multi-turn conversations about video content** using semantic retrieval and LLMs.

---

## 🚀 Features

* Extracts **YouTube video transcripts automatically**
* Converts transcripts into **semantic chunks**
* Generates **vector embeddings using OpenAI**
* Stores vectors in a **FAISS vector database**
* Uses **Retrieval-Augmented Generation (RAG)** for context-grounded answers
* Supports **question answering and video summarization**
* Maintains **conversation memory for follow-up questions**
* Supports **multi-user sessions with isolated chat histories**

---

## 🏗 System Architecture

User Query
↓
Session-based Chat Memory
↓
Retriever (FAISS similarity search)
↓
Relevant Transcript Chunks
↓
Prompt Template (Context + Chat History)
↓
LLM (GPT-4o-mini)
↓
Final Answer / Summary

---

## ⚙️ Tech Stack

* **Python**
* **LangChain (Runnable-based pipelines)**
* **OpenAI API (GPT-4o-mini, text-embedding-3-small)**
* **FAISS Vector Database**
* **YouTube Transcript API**
* **Retrieval-Augmented Generation (RAG)**
* **Session-based Conversation Memory**

---

## 📂 Project Structure

```
youtube-rag-system/
│
├── app.py                     # Main application
├── src/
│   ├── transcript_loader.py  # Fetch YouTube captions
│   ├── text_splitter.py      # Chunk transcript text
│   ├── embeddings.py         # Embedding model
│   ├── vector_store.py       # FAISS vector store
│   ├── retriever.py          # Document retriever
│   └── rag_chain.py          # RAG pipeline
│
├── utils/
│   └── youtube_utils.py      # Extract YouTube video ID
│
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠 Installation

Clone the repository

```
git clone https://github.com/bhoopenderbaghel/YouTube-Video-QA-Chatbot.git
cd YouTube-Video-QA-Chatbot
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

Enter a YouTube video URL and start asking questions about the video.

Example queries:

```
Can you summarize the video?
What topics are discussed?
Explain the concept of attention mentioned in the video.
```

You can also ask **follow-up questions**, and the system will use conversation history to maintain context.

---

## 📌 Example Use Cases

* Summarizing long educational videos
* Asking questions about lecture content
* Extracting key insights from technical talks
* Conversational exploration of video knowledge
* Building searchable video knowledge bases

---

## 📈 Future Improvements

* Add **Streamlit UI for an interactive chatbot**
* Implement **persistent FAISS vector storage per video**
* Add **hybrid search (BM25 + vector retrieval)**
* Support **automatic transcript translation for multilingual videos**
* Deploy as an **API or web application**

---

## 👤 Author

**Bhoopender Baghel**

AI / GenAI Projects