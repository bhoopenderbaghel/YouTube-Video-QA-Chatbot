from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def create_rag_chain(retriever):

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    prompt = PromptTemplate(
        template="""
You are a helpful assistant.

Answer ONLY from the provided transcript context.

Chat History:
{chat_history}

Context:
{context}

Question:
{question}
""",
        input_variables=["chat_history", "context", "question"]
    )

    parallel = RunnableParallel({
        "question": RunnableLambda(lambda x: x["question"]),
        "context": RunnableLambda(lambda x: x["question"]) | retriever | RunnableLambda(format_docs),
        "chat_history": RunnableLambda(lambda x: x["chat_history"])
    })

    parser = StrOutputParser()

    chain = parallel | prompt | llm | parser

    return chain