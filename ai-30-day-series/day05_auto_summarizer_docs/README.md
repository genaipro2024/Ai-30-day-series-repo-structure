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
