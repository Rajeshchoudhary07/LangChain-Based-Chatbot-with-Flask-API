from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI

def create_chatbot(vectorstore):
    retriever = vectorstore.as_retriever()
    return ConversationalRetrievalChain.from_llm(OpenAI(), retriever)
