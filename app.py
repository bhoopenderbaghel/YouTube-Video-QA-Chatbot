from dotenv import load_dotenv
from src.transcript_loader import get_transcript
from src.text_splitter import split_text
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.rag_chain import create_rag_chain
from utils.youtube_utils import extract_video_id

load_dotenv()


url = input("Enter YouTube URL: ")

video_id = extract_video_id(url)

transcript = get_transcript(video_id)

docs = split_text(transcript)

embedding = get_embedding_model()

vector_store = create_vector_store(docs, embedding)

retriever = get_retriever(vector_store)

rag_chain = create_rag_chain(retriever)

question = input("Ask a question: ")

answer = rag_chain.invoke(question)

print(answer)