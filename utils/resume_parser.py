import re
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception:
        return ""

def extract_name_and_email(resume_text):
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', resume_text)
    email = email_match.group(0) if email_match else None

    lines = resume_text.strip().split('\n')
    name = None
    for line in lines:
        if line.strip() and not any(x in line.lower() for x in ['email', 'phone', '@', 'www']):
            name = line.strip()
            break

    return name, email
