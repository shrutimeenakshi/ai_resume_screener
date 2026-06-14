# 🤖 AI Resume Screening System

An AI-powered Resume Screening and Candidate Shortlisting platform developed using Flask, Python, NLP, and SQL. The system automates resume analysis by matching candidate resumes against job descriptions and generating intelligent match scores for efficient hiring decisions.

The platform helps HR teams and recruiters streamline the recruitment process by reducing manual screening efforts and improving candidate selection accuracy.

---

# 🚀 Features

✅ Resume upload and parsing
✅ AI-powered Job Description (JD) matching
✅ Automated resume scoring system
✅ NLP-based skill extraction
✅ Candidate shortlisting
✅ Admin dashboard for HR management
✅ Resume filtering and search
✅ Bulk resume upload support
✅ Resume download functionality
✅ Send selected resumes to Talent Acquisition (TA) team
✅ Match percentage visualization
✅ Database integration for resume storage

---

# 🛠️ Tech Stack

| Category         | Technologies                               |
| ---------------- | ------------------------------------------ |
| Backend          | Python, Flask                              |
| Frontend         | HTML, CSS, Bootstrap, JavaScript           |
| Database         | SQLite / SQLAlchemy                        |
| AI/NLP           | NLP, Resume Parsing                        |
| Authentication   | Flask Login / JWT                          |
| Additional Tools | PDF Processing, Resume Matching Algorithms |

---

# 📂 Project Structure

```plaintext id="g9q8dt"
AI-Resume-Screener/
│
├── static/                  # CSS, JavaScript, assets
├── templates/               # HTML templates and UI pages
├── uploads/                 # Uploaded resumes
├── utils/                   # Resume parsing and matching logic
├── app.py                   # Main Flask application
├── database.db              # SQLite database
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

# 👨‍💻 System Modules

## 🔹 Admin Module

The administrator can:

* Login securely
* Upload Job Descriptions
* Filter resumes based on match score
* View shortlisted candidates
* Download resumes
* Send selected resumes to TA team
* Manage uploaded candidate data

---

## 🔹 Resume Screening Module

This module handles:

* Resume parsing
* Text extraction from PDF resumes
* Skill extraction using NLP
* Job Description matching
* Candidate score generation
* Resume ranking and filtering

---

## 🔹 Candidate Management Module

Features include:

* Resume database storage
* Candidate detail tracking
* Match percentage visualization
* Resume categorization
* Bulk resume management

---

# 🔄 System Workflow

1. Admin uploads a Job Description (JD)
2. Candidates upload their resumes in PDF format
3. The system extracts resume content using NLP techniques
4. Skills and keywords are matched with the uploaded JD
5. Match scores are calculated automatically
6. Candidates are ranked based on compatibility
7. Admin filters and shortlists suitable candidates
8. Selected resumes are forwarded to the Talent Acquisition (TA) team

---

# 📊 Key Functionalities

## 📄 Resume Parsing

Extracts text and candidate information from uploaded resumes.

## 🧠 AI-Based Matching

Compares resumes against job descriptions using NLP and keyword analysis.

## 📈 Candidate Scoring

Generates a compatibility score based on skills, experience, and JD matching.

## 🎯 Smart Filtering

Allows recruiters to shortlist candidates efficiently using filters.

## 📥 Resume Management

Stores and manages uploaded resumes in the database.

---

# 🗄️ Database

The system stores:

* Candidate details
* Uploaded resumes
* Match scores
* Job descriptions
* Screening results
* Admin data

---

# ⚙️ Installation

## Clone the Repository

```bash id="9b9n16"
git clone https://github.com/shrutimeenakshi/ai_resume_screener.git
```

---

## Navigate to Project Folder

```bash id="eijg1i"
cd ai_resume_screener
```

---

## Create Virtual Environment

```bash id="94i4b6"
python -m venv venv
```

Activate the environment:

### Windows

```bash id="psu3qt"
venv\Scripts\activate
```

### macOS/Linux

```bash id="6ycjlwm"
source venv/bin/activate
```

---

## Install Dependencies

```bash id="7q3jlu"
pip install -r requirements.txt
```

---

## Run the Application

```bash id="dyvflk"
python app.py
```

---

## Open in Browser

```plaintext id="uynk7q"
http://127.0.0.1:5000/
```


---

# 🎯 Objectives

* Automate resume screening process
* Reduce manual hiring effort
* Improve recruitment efficiency
* Enable AI-based candidate analysis
* Provide accurate JD-resume matching
* Simplify candidate shortlisting

---

# 🔮 Future Enhancements

* AI-generated interview questions
* Email notification system
* Cloud deployment
* Advanced analytics dashboard
* Multi-role authentication
* Machine Learning-based candidate ranking
* Real-time recruitment analytics

---

# 📚 Learning Outcomes

* Flask backend development
* NLP implementation
* Resume parsing techniques
* Database integration
* Admin dashboard development
* AI-based filtering systems
* Automation workflow design
* REST API integration

---

# 🔐 Security Improvements

Future improvements may include:

* Secure authentication system
* Role-based access control
* Encrypted resume storage
* HTTPS deployment
* Cloud database integration

---

# 🌟 Applications

* Recruitment automation
* HR management systems
* Talent acquisition platforms
* AI hiring solutions
* Candidate shortlisting systems

---
