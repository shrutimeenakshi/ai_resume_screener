# AI-Based Resume Screening System

This is a smart recruitment tool that automates resume screening using AI. It parses PDF resumes, matches them against job descriptions, and highlights key skill matches — helping HR teams shortlist the best-fit candidates efficiently.

## 🚀 Features

- ✅ Admin login for secure access
- ✅ Upload Job Description (JD)
- ✅ Upload multiple resumes
- ✅ AI matching algorithm (Python, NLP-based)
- ✅ Skill extraction and matching
- ✅ Score-based ranking
- ✅ Dashboard to view all results
- ✅ "Send to TA" & "Download Resume" options

## 💡 Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Libraries:** PyPDF2, spaCy, NLTK, SQLAlchemy
- **Version Control:** Git + GitHub

## 📂 Project Structure

ai_resume_screener/
│
├── app.py # Main Flask App
├── templates/ # HTML Pages (login, dashboard, results)
├── static/ # CSS styling
├── utils/ # Resume parser & matching logic
├── db/ # SQLite database
├── resumes/ # Sample resumes
├── uploads/ # Uploaded resumes
├── requirements.txt # Python dependencies



## 🧠 AI Resume Matching Logic

Each resume is parsed and compared against the job description. A similarity score is calculated based on:
- Skill match
- Experience keywords
- Job role relevance

## 🛠 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/shrutimeenakshi/ai_resume_screener.git

# Navigate into the folder
cd ai_resume_screener

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
