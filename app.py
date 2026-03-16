from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv
from src.transcript_loader import get_transcript
from src.text_splitter import split_text
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.rag_chain import create_rag_chain
from utils.youtube_utils import extract_video_id


load_dotenv()


store = {}

def get_session_history(session_id):

    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


url = input("Enter YouTube URL: ")

video_id = extract_video_id(url)

transcript = get_transcript(video_id)

docs = split_text(transcript)

embedding = get_embedding_model()

vector_store = create_vector_store(docs, embedding)

retriever = get_retriever(vector_store)

rag_chain = create_rag_chain(retriever)


rag_with_memory = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="chat_history",
)


session_id = input("Enter user id: ")


while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer = rag_with_memory.invoke(
        {"question": question},
        config={"configurable": {"session_id": session_id}}
    )

    print("\nAI:", answer)

    print(store)