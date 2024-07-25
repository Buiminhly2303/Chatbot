from config import GOOGLE_API_KEY
import os

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

from langchain_google_genai import GoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings

model_kwargs = {'device': 'cpu'}
model_kwargs=model_kwargs

llm = GoogleGenerativeAI(model="gemini-pro")
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3", model_kwargs=model_kwargs)
print("Done Load Model!")
