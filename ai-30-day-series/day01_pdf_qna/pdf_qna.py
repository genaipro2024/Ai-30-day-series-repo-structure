import os
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "your-api-key"

loader = PyPDFLoader("sample.pdf")
documents = loader.load_and_split()
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents, embedding)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4"),
    retriever=vectordb.as_retriever(),
)

question = "What is this document about?"
result = qa.run(question)
print(result)