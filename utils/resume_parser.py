import re

from pdfminer.high_level import extract_text

from docx import Document


# =========================
# PDF TEXT EXTRACTION
# =========================

def extract_text_from_pdf(pdf_path):

    try:

        return extract_text(pdf_path)

    except Exception:

        return ""


# =========================
# DOCX TEXT EXTRACTION
# =========================

def extract_text_from_docx(docx_path):

    try:

        doc = Document(docx_path)

        full_text = []

        for para in doc.paragraphs:

            full_text.append(para.text)

        return "\n".join(full_text)

    except Exception:

        return ""


# =========================
# NAME + EMAIL EXTRACTION
# =========================

def extract_name_and_email(resume_text):

    # Extract email
    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        resume_text
    )

    email = email_match.group(0) \
        if email_match else None

    # Extract name
    lines = resume_text.strip().split('\n')

    name = None

    for line in lines:

        if (
            line.strip() and
            not any(
                x in line.lower()
                for x in [
                    'email',
                    'phone',
                    '@',
                    'www'
                ]
            )
        ):

            name = line.strip()

            break

    return name, email