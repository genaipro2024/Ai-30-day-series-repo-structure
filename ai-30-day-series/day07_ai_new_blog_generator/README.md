# 🧠 Day 7 – AI Blog Generator from Keywords

Turn 3–5 keywords into a full SEO-friendly blog article using OpenAI and LangChain.

---

## 📦 Features

- Input: Keywords (e.g., "AI, education, India")
- Output: Markdown-formatted blog with title, intro, subheadings, and conclusion
- Tech: Python, LangChain, OpenAI
- Tone: Professional and informative
- Output is ready for Medium or Dev.to!

---

## 🚀 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourgithub/30DaysOfAI.git
cd 30DaysOfAI/days/day07

### 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install langchain openai
### 4. Add your OpenAI API key
Create a .env file or export manually:


export OPENAI_API_KEY=your-key-here
Or replace "your-openai-key" directly in index.py.


💡 Usage
python index.py
Example input:


Enter your keywords (comma-separated): AI, Healthcare, India
Example output:


# How AI is Revolutionizing Healthcare in India
...
📝 Sample Output

# How AI is Revolutionizing Healthcare in India

## Introduction
AI is transforming Indian healthcare by improving diagnosis and rural access...

## Improving Diagnosis
...

## Rural Accessibility
...

## Cost Efficiency
...

## Conclusion
AI is no longer the future — it's the now.