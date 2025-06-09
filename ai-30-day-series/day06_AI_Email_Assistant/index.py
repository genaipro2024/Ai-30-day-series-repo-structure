
---

## 🐍 Python File — `index.py`

```python
# index.py — AI Email Assistant

import imaplib
import email
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

EMAIL = "you@gmail.com"
APP_PASSWORD = "your-app-password"

def fetch_latest_emails(username, password, n=5):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    result, data = mail.search(None, "UNSEEN")
    mail_ids = data[0].split()[-n:]

    emails = []
    for id in mail_ids:
        result, msg_data = mail.fetch(id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()
        emails.append((msg["From"], msg["Subject"], body.strip()))
    return emails

llm = OpenAI()

summary_prompt = PromptTemplate.from_template("""
Summarize this email in 3 bullet points:
{email}
""")

reply_prompt = PromptTemplate.from_template("""
Suggest a professional reply to this email:
{email}
""")

def summarize_and_reply(email_body):
    summary = llm(summary_prompt.format(email=email_body))
    reply = llm(reply_prompt.format(email=email_body))
    return summary.strip(), reply.strip()

if __name__ == "__main__":
    emails = fetch_latest_emails(EMAIL, APP_PASSWORD, n=3)

    for i, (sender, subject, body) in enumerate(emails):
        print(f"\n📨 Email {i+1} from {sender} — {subject}")
        summary, reply = summarize_and_reply(body)
        print("\n📝 Summary:\n", summary)
        print("\n✍️ Suggested Reply:\n", reply)
