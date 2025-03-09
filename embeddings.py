from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def create_vector_store(docs, persist_directory="chroma_store"):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    vectorstore.persist()
    return vectorstore
