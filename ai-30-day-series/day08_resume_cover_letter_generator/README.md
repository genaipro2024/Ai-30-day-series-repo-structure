# 🧠 Day 8 – AI Cover Letter Generator (from Resume + Job Description)

Generate a personalized cover letter using just your resume and a job description — in seconds, using OpenAI + LangChain.

---

## 🚀 Features

- 📄 Read any resume PDF
- 📋 Accepts job description via CLI
- 🤖 Uses OpenAI to create a confident, professional cover letter
- 🎯 Output ready to copy into your job application

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourgithub/30DaysOfAI.git
cd 30DaysOfAI/days/day08

2. Set up a virtual environment (optional but recommended)
 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Python dependencies
 
pip install langchain openai pdfplumber

4. Set your OpenAI API Key
Add it directly in the script or via environment variable:

 
export OPENAI_API_KEY=your-key-here
You can also use a .env file and python-dotenv if preferred.

▶️ Usage
Run the program:

bash
python index.py
You will be prompted to:
Enter path to your resume (PDF)

Paste the job description (end with a blank line)

💡 Example:

bash
Enter path to resume PDF file (e.g. resume.pdf): my_resume.pdf

Paste your job description below. End input with a blank line:

We are hiring a Senior Software Engineer with 5+ years of Python, Django, and cloud experience...
[Press Enter twice]
✅ Output Example
css
Dear Hiring Manager,

I’m thrilled to apply for the Senior Software Engineer role at [Company]. With 6+ years of backend experience in Python and AWS...

I’d love to bring my skills and passion to your team.

Sincerely,  
Your Name
🔗 Links
🔗 GitHub Repo

✍️ Medium Blog Post