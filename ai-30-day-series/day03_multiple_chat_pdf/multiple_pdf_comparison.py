from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

pdfs = ['contract1.pdf', 'contract2.pdf']
pages = []
for file in pdfs:
    loader = PyPDFLoader(file)
    pages += loader.load()

vectorstore = FAISS.from_documents(pages, OpenAIEmbeddings())
qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=vectorstore.as_retriever())

query = "Compare the contract duration clauses."
print(qa.run(query))