📘 README.md


# 🐦 Day 9 – Blog to Twitter Thread Generator

Use AI to instantly convert a blog post into a polished, viral-style Twitter thread.  
Built with Python, OpenAI, LangChain, and BeautifulSoup.

---

## 💡 What It Does

- Fetches text from any blog URL
- Uses AI to convert blog into 8–10 tweets
- Includes hook, body, and CTA
- Great for writers, marketers, and indie hackers

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourgithub/30DaysOfAI.git
cd 30DaysOfAI/days/day09
2. Set up virtual environment (optional)
bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bash

pip install langchain openai beautifulsoup4 requests
4. Set your OpenAI key
bash

export OPENAI_API_KEY=your-key-here  # or use .env + dotenv
▶️ Usage
bash

python index.py
You'll be prompted to enter the blog URL (e.g., https://yourblog.com/post).

Example output:



Tweet 1: Writing long blogs but getting 0 engagement? Here's how to convert them into viral threads 🧵

Tweet 2: Step 1: Start with a hook...

...

Tweet 10: Follow me for more daily AI tools 🚀
