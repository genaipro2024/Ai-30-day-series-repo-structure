# 📬 Day 6 – AI Email Assistant (30 Days of AI)

Automatically read, summarize, and generate replies to your Gmail using OpenAI.

---

## 🧠 Features

- Connects to your Gmail (via IMAP)
- Pulls recent unread emails
- Summarizes them in 3 bullet points
- Suggests polite, professional replies

---

## 🛠️ Setup

1. **Enable IMAP** in Gmail  
2. Create an **App Password**  
   [How to create one →](https://support.google.com/mail/answer/185833)

---

## 📦 Installation

```bash
python -m venv venv
source venv/bin/activate

pip install langchain openai

🚀 Run It
Put your credentials in the code (index.py):

 
python index.py
🧠 Output Sample
 
📨 Email from raj@client.com — Request for Update

📝 Summary:
- Asking about project timeline
- Wants confirmation on delivery
- Suggests call this Friday

✍️ Suggested Reply:
Thanks Raj, delivery is on track. Friday call works. Let me know timing.