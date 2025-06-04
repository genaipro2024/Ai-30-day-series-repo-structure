import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

loader = PyPDFLoader("sample.pdf")
documents = loader.load_and_split()
vectordb = Chroma.from_documents(documents, OpenAIEmbeddings())
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4"),
    retriever=vectordb.as_retriever(),
)

recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    print("🤖", text)
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Ask something about the PDF...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        return ""

while True:
    query = listen()
    if query:
        answer = qa.run(query)
        speak(answer)