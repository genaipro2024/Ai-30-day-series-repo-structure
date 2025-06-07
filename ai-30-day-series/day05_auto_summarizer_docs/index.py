# Day 5 – Auto-Summarizer for Long Documents using AI

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain

# STEP 1: Load your document (plain text for now)
with open("sample.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

# STEP 2: Split into smaller chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
docs = splitter.create_documents([full_text])

# STEP 3: Create a vector store (optional if you're only summarizing)
db = FAISS.from_documents(docs, OpenAIEmbeddings())

# STEP 4: Create and run summarization chain
llm = OpenAI()
chain = load_summarize_chain(llm, chain_type="map_reduce")
summary = chain.run(docs)

# STEP 5: Print the output
print("📄 Summary of the Document:\n")
print(summary)
