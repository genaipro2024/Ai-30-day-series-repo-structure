# index.py

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-key"  # Replace or set via .env

# Initialize the LLM
llm = OpenAI(temperature=0.7)

# Define a prompt template for generating blog posts
blog_prompt = PromptTemplate.from_template("""
You are a professional blog writer.

Write a detailed blog post on the topic using these keywords:
{keywords}

The blog should include:
- A catchy title
- Introduction
- At least 3 subheadings
- A short conclusion
- Tone: Professional and informative

Use markdown formatting.
""")

def generate_blog(keywords):
    prompt = blog_prompt.format(keywords=keywords)
    return llm(prompt)

if __name__ == "__main__":
    user_keywords = input("Enter your keywords (comma-separated): ")
    blog_output = generate_blog(user_keywords)
    print("\n📝 Generated Blog Post:\n")
    print(blog_output)
