# 📘 Day 5 – Auto-Summarizer for Long Documents (30 Days of AI)

This project lets you **upload a long text document and get an instant summary** using OpenAI and LangChain.

---

## 🧠 What It Does

- Reads your `.txt` or `.pdf` file  
- Splits the document into chunks  
- Uses OpenAI to generate a summary  
- Outputs a TL;DR instantly

---

## 🛠️ Installation

```bash
# Create virtual env (optional)
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install langchain openai faiss-cpu pdfplumber

🚀 Run the Script
Put your long text in sample.txt (UTF-8 encoded), then:

python index.py
You’ll see the summary printed in your terminal.

🔄 Customize
To support PDF: use pdfplumber to extract text

To use local LLM (like Llama2): swap OpenAI() with a local chain using llama-cpp or ollama

