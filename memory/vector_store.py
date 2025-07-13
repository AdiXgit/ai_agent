from langchain.vectorstores import Chroma 
from langchain.embeddings import OllamaEmbeddings

def get_vector():
    return Chroma(
        persist_directory="data/chroma",
        embedding_function=OllamaEmbeddings(model = "mistral:latest"),
    )

