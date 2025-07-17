import re

def extract_jd_info(jd_text):
    jd_info = {
        'primary_skills': [],
        'secondary_skills': [],
        'location': '',
        'experience': 0,
        'qualification': [],
        'max_age': 100
    }

    # Extract skills
    primary_match = re.search(r'Primary Skills:\s*(.+)', jd_text, re.IGNORECASE)
    secondary_match = re.search(r'Secondary Skills:\s*(.+)', jd_text, re.IGNORECASE)
    location_match = re.search(r'Location:\s*(.+)', jd_text, re.IGNORECASE)
    exp_match = re.search(r'Experience:\s*(\d+)', jd_text, re.IGNORECASE)
    qual_match = re.search(r'Qualification:\s*(.+)', jd_text, re.IGNORECASE)
    age_match = re.search(r'Age:\s*[<≤]?\s*(\d+)', jd_text, re.IGNORECASE)

    if primary_match:
        jd_info['primary_skills'] = [s.strip().lower() for s in primary_match.group(1).split(',')]
    if secondary_match:
        jd_info['secondary_skills'] = [s.strip().lower() for s in secondary_match.group(1).split(',')]
    if location_match:
        jd_info['location'] = location_match.group(1).strip()
    if exp_match:
        jd_info['experience'] = int(exp_match.group(1))
    if qual_match:
        jd_info['qualification'] = [q.strip().lower() for q in qual_match.group(1).split(',')]
    if age_match:
        jd_info['max_age'] = int(age_match.group(1))

    return jd_info


def extract_resume_info(resume_text):
    resume_text_lower = resume_text.lower()

    # Dummy skill extraction (replace with spaCy/NLP for better accuracy)
    skills = re.findall(r'\b[a-zA-Z]{2,}\b', resume_text_lower)
    skills = list(set(skills))

    # Dummy location and qualification extraction
    location = "unknown"
    if "chennai" in resume_text_lower:
        location = "chennai"

    qualification = []
    if "b.tech" in resume_text_lower or "bachelor of technology" in resume_text_lower:
        qualification.append("b.tech")
    if "b.e" in resume_text_lower:
        qualification.append("b.e")

    # Experience (look for patterns like "3 years", "5+ years", etc.)
    exp_match = re.search(r'(\d+)\+?\s+years', resume_text_lower)
    experience = int(exp_match.group(1)) if exp_match else 0

    # Age (if DOB or age is mentioned)
    age = None
    age_match = re.search(r'age\s*[:\-]?\s*(\d+)', resume_text_lower)
    if age_match:
        age = int(age_match.group(1))

    return {
        'skills': skills,
        'location': location,
        'qualification': qualification,
        'experience': experience,
        'age': age
    }


def match_resume_with_jd(resume_text, jd_text):
    jd_info = extract_jd_info(jd_text)
    resume_info = extract_resume_info(resume_text)

    score = 0
    matched = []

    # Primary skills
    for skill in jd_info['primary_skills']:
        if skill in resume_info['skills']:
            score += 20
            matched.append(skill)

    # Secondary skills
    for skill in jd_info['secondary_skills']:
        if skill in resume_info['skills']:
            score += 10
            matched.append(skill)

    # Location
    if jd_info['location'].lower() in resume_info['location'].lower():
        score += 10

    # Experience
    if resume_info['experience'] >= jd_info['experience']:
        score += 10

    # Qualification
    if any(q in resume_info['qualification'] for q in jd_info['qualification']):
        score += 10

    # Age
    if resume_info['age'] is not None and resume_info['age'] <= jd_info['max_age']:
        score += 10

    return min(score, 100), matched
