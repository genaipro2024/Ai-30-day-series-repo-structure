# 🎥 Day 4 – Chat with a YouTube Video Using AI

This AI agent lets you input a YouTube video ID and ask questions like:

- "Summarize the talk"
- "What tools were mentioned?"
- "What's the speaker’s opinion on AGI?"

---

## 🧰 Tech Stack

- [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) – fetch subtitles
- [`langchain`](https://python.langchain.com/) – manage LLM + retrieval chain
- [`openai`](https://platform.openai.com/docs) – language model
- [`faiss-cpu`](https://github.com/facebookresearch/faiss) – vector DB

---

## ⚙️ Installation

```bash
# Create a virtual environment (optional)
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install youtube-transcript-api langchain openai faiss-cpu


🚀 Run the App

python implementation.py


Example inputs:
 
Enter YouTube video ID (e.g., dQw4w9WgXcQ): yKjQGzpm7Vk
Ask your question: What are the speaker's main points?


🧠 Sample Output
 
✅ Answer:
- The speaker emphasizes the importance of open AI development.
- Discusses alignment and transparency.
- Predicts rapid growth of AGI models.