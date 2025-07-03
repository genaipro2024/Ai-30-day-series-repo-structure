# index.py

import os
import requests
from bs4 import BeautifulSoup
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-key"  # Replace this or use dotenv

# Load the LLM
llm = OpenAI(temperature=0.7)

# Define the Twitter thread generation prompt
thread_prompt = PromptTemplate.from_template("""
You are a professional social media content writer.

Turn this blog post into a viral Twitter/X thread.

Use:
- A strong hook tweet (Tweet 1)
- 8–10 tweets that summarize the blog clearly
- A closing call-to-action or quote

Input blog post:
{blog}

Output format:
Tweet 1: ...
Tweet 2: ...
...
Tweet 10: ...
""")

def fetch_blog_text(url):
    """Fetch blog text from a given URL using BeautifulSoup."""
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        paragraphs = soup.find_all('p')
        return "\n".join([p.text for p in paragraphs if p.text.strip()])
    except Exception as e:
        return f"Error fetching blog: {str(e)}"

def generate_thread(blog_text):
    prompt = thread_prompt.format(blog=blog_text)
    return llm(prompt)

if __name__ == "__main__":
    blog_url = input("Enter blog URL: ").strip()
    print("\n⏳ Fetching blog content...")
    blog_text = fetch_blog_text(blog_url)

    print("✍️ Generating Twitter thread...\n")
    thread_output = generate_thread(blog_text)

    print("🧵 AI-Generated Twitter Thread:\n")
    print(thread_output)
