# implementation.py - Day 4: Chat with a YouTube Video using AI

from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Step 1: Get the transcript of the YouTube video
def fetch_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return "\n".join([item['text'] for item in transcript])

# Step 2: Chunk the transcript and embed
def embed_transcript(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    return db

# Step 3: Create QA chain
def create_qa_chain(db):
    return RetrievalQA.from_chain_type(llm=OpenAI(), retriever=db.as_retriever())

# Step 4: Ask questions
def ask_question(chain, question):
    return chain.run(question)

# 🔽 Main script
if __name__ == "__main__":
    video_id = input("Enter YouTube video ID (e.g., dQw4w9WgXcQ): ").strip()
    query = input("Ask your question: ").strip()

    print("🔍 Fetching transcript...")
    text = fetch_transcript(video_id)

    print("📚 Creating vector database...")
    db = embed_transcript(text)

    print("💬 Running QA...")
    chain = create_qa_chain(db)
    answer = ask_question(chain, query)

    print("\n✅ Answer:")
    print(answer)
