# index.py
import os
import pdfplumber
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Optional: Use .env to load secret keys
os.environ["OPENAI_API_KEY"] = "your-openai-key"  # or use dotenv

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.7)

# Prompt Template for Cover Letter
cover_letter_prompt = PromptTemplate.from_template("""
You are a professional career assistant.

Based on this resume:
{resume}

And this job description:
{jd}

Write a personalized and professional cover letter. It should:
- Address the hiring manager
- Match the candidate's skills to the job
- Sound confident and concise
""")

# Function to extract text from PDF resume
def extract_resume_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# Function to generate cover letter using LangChain + LLM
def generate_cover_letter(resume_text, job_description):
    prompt = cover_letter_prompt.format(resume=resume_text, jd=job_description)
    return llm(prompt)

if __name__ == "__main__":
    # --- Input Section ---
    resume_file = input("Enter path to resume PDF file (e.g. resume.pdf): ").strip()
    print("\nPaste your job description below. End input with a blank line:\n")
    jd_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        jd_lines.append(line)
    job_description = "\n".join(jd_lines)

    # --- Processing Section ---
    print("\n📄 Reading resume...")
    resume_text = extract_resume_text(resume_file)

    print("✍️ Generating personalized cover letter...\n")
    letter = generate_cover_letter(resume_text, job_description)

    print("✅ Generated Cover Letter:\n")
    print(letter)
