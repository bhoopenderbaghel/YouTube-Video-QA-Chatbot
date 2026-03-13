from langchain_community.vectorstores import FAISS

def create_vector_store(docs, embedding):

    vector_store = FAISS.from_documents(
        docs,
        embedding
    )

    return vector_store