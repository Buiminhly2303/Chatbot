import os
import sys
import pandas as pd

sys.path.append("../")

from model import embeddings
from qdrant_client import QdrantClient
from langchain_community.vectorstores import Qdrant

from config import QDRANT_HOST, QDRANT_PORT, DOCUMENT_PATHS
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import CharacterTextSplitter



def build_vector_store(collection_name='MyCollection'):
    # Ensure DOCUMENT_PATHS points to the folder containing CSV files
    loader = TextLoader(DOCUMENT_PATHS)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Initialize the Qdrant client
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    
    # Define the collection name
    collection_name = collection_name
    
    # Create a Qdrant vector store
    vectorstore = QdrantVectorStore.from_documents(
        docs,
        embeddings,
        url='http://0.0.0.0:6333',
        prefer_grpc=True,
        collection_name=collection_name,
        force_recreate=True,
    )

    print("Done build vector store!")
    return vectorstore
