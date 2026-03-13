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
        Answer ONLY from the provided context.

        {context}

        Question: {question}
        """,
        input_variables=["context","question"]
    )

    parallel = RunnableParallel({
        "question": RunnablePassthrough(),
        "context": retriever | RunnableLambda(format_docs)
    })

    parser = StrOutputParser()

    chain = parallel | prompt | llm | parser

    return chain