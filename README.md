# 🤖 AI-Powered Resume Screening and ATS Ranking System

An AI-powered Resume Screening and Candidate Ranking System developed using Flask, Python, NLP, Machine Learning, and SQLite. The platform automates resume analysis by intelligently matching resumes with job descriptions, predicting candidate roles, and ranking applicants based on compatibility scores.

The system helps recruiters and HR teams streamline the hiring process by reducing manual screening efforts and improving candidate shortlisting accuracy.

---

# 🚀 Features

✅ Resume Upload and Parsing
✅ PDF and DOCX Resume Support
✅ AI-Based Resume Classification
✅ Logistic Regression ML Model
✅ TF-IDF Vectorization
✅ Cosine Similarity Matching
✅ Automated Resume Ranking
✅ Confidence Score Prediction
✅ ATS-Style Candidate Screening
✅ Top Candidate Highlighting
✅ Job Description (JD) Matching
✅ Admin Dashboard for Recruiters
✅ Resume Download Functionality
✅ Candidate Shortlisting
✅ Bulk Resume Upload Support
✅ Database Integration using SQLite

---

# 🛠️ Tech Stack

| Category         | Technologies                     |
| ---------------- | -------------------------------- |
| Backend          | Python, Flask                    |
| Frontend         | HTML, CSS, Bootstrap, JavaScript |
| Database         | SQLite, SQLAlchemy               |
| Machine Learning | Logistic Regression              |
| NLP Techniques   | TF-IDF, Cosine Similarity        |
| Resume Parsing   | PDFMiner, python-docx            |
| Tools            | Git, GitHub                      |

---

# 🧠 AI / ML Workflow

1. Resume is uploaded in PDF or DOCX format
2. Resume text is extracted automatically
3. TF-IDF vectorization converts text into numerical vectors
4. Logistic Regression predicts candidate job role
5. Cosine Similarity compares resume with Job Description
6. Match score and confidence score are generated
7. Candidates are ranked automatically
8. Top candidate is highlighted for recruiters

---

# 📂 Project Structure

```bash
AI_RESUME_SCREENER/
│
├── static/
├── templates/
├── utils/
├── resumes/
├── db/
│
├── app.py
├── train_model.py
├── resume_dataset.csv
├── resume_classifier.pkl
├── requirements.txt
├── README.md
```

---

# 👨‍💻 System Modules

## 🔹 Resume Parsing Module

* Extracts text from PDF and DOCX resumes
* Extracts candidate details
* Performs preprocessing for NLP

---

## 🔹 AI Resume Classification Module

* Uses Logistic Regression for role prediction
* Predicts categories like:

  * Frontend Developer
  * DevOps Engineer
  * Data Analyst
  * ML Engineer
  * UI/UX Designer

---

## 🔹 ATS Matching Module

* Performs JD-resume similarity analysis
* Calculates compatibility scores
* Ranks candidates automatically

---

## 🔹 Admin Dashboard

Recruiters can:

* View uploaded resumes
* Filter candidates
* Download resumes
* Shortlist candidates
* View top-ranked applicants

---

# 📊 Key Functionalities

## 📄 Resume Parsing

Automatically extracts text from uploaded resumes.

---

## 🧠 AI-Based Classification

Uses Machine Learning to classify resumes into job roles.

---

## 📈 Resume Ranking

Ranks resumes using cosine similarity and JD matching.

---

## 🎯 Candidate Shortlisting

Highlights top candidates based on compatibility score.

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/shrutimeenakshi/ai_resume_screener.git
```

---

## Navigate to Project Folder

```bash
cd ai_resume_screener
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

## Open in Browser

```bash
http://127.0.0.1:5000/
```

---

# 🎯 Objectives

* Automate resume screening
* Reduce manual hiring effort
* Improve recruitment efficiency
* Implement AI-based candidate analysis
* Enable intelligent JD-resume matching
* Build an ATS-style recruitment system

---

# 🔮 Future Enhancements

* Deep Learning-based resume analysis
* AI-generated interview questions
* Email notification integration
* Cloud deployment
* Advanced recruiter analytics
* Multi-user authentication
* Real-time hiring dashboard

---

# 📚 Learning Outcomes

* Flask Backend Development
* Machine Learning Integration
* NLP Text Processing
* Resume Parsing Techniques
* TF-IDF Vectorization
* Logistic Regression Classification
* Cosine Similarity Matching
* Database Integration
* Full Stack Development

---

# 🌟 Applications

* Recruitment Automation
* HR Management Systems
* Talent Acquisition Platforms
* AI Hiring Solutions
* ATS Resume Screening Systems

---

