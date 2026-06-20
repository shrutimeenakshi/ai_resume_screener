import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_jd_info(jd_text):

    jd_info = {
        'primary_skills': [],
        'secondary_skills': [],
        'location': '',
        'experience': 0,
        'qualification': [],
        'max_age': 100
    }

    # Extract primary skills
    primary_match = re.search(
        r'Primary Skills:\s*(.+)',
        jd_text,
        re.IGNORECASE
    )

    # Extract secondary skills
    secondary_match = re.search(
        r'Secondary Skills:\s*(.+)',
        jd_text,
        re.IGNORECASE
    )

    # Extract location
    location_match = re.search(
        r'Location:\s*(.+)',
        jd_text,
        re.IGNORECASE
    )

    # Extract experience
    exp_match = re.search(
        r'Experience:\s*(\d+)',
        jd_text,
        re.IGNORECASE
    )

    # Extract qualification
    qual_match = re.search(
        r'Qualification:\s*(.+)',
        jd_text,
        re.IGNORECASE
    )

    # Extract age
    age_match = re.search(
        r'Age:\s*[<≤]?\s*(\d+)',
        jd_text,
        re.IGNORECASE
    )

    if primary_match:
        jd_info['primary_skills'] = [
            s.strip().lower()
            for s in primary_match.group(1).split(',')
        ]

    if secondary_match:
        jd_info['secondary_skills'] = [
            s.strip().lower()
            for s in secondary_match.group(1).split(',')
        ]

    if location_match:
        jd_info['location'] = location_match.group(1).strip().lower()

    if exp_match:
        jd_info['experience'] = int(exp_match.group(1))

    if qual_match:
        jd_info['qualification'] = [
            q.strip().lower()
            for q in qual_match.group(1).split(',')
        ]

    if age_match:
        jd_info['max_age'] = int(age_match.group(1))

    return jd_info


def extract_resume_info(resume_text):

    resume_text_lower = resume_text.lower()

    # Extract words as skills
    skills = re.findall(r'\b[a-zA-Z][a-zA-Z\+\#\.]+\b', resume_text_lower)

    skills = list(set(skills))

    # Extract location
    location = "unknown"

    if "chennai" in resume_text_lower:
        location = "chennai"

    # Qualification extraction
    qualification = []

    if "b.tech" in resume_text_lower or "bachelor of technology" in resume_text_lower:
        qualification.append("b.tech")

    if "b.e" in resume_text_lower:
        qualification.append("b.e")

    # Experience extraction
    exp_match = re.search(
        r'(\d+)\+?\s+years',
        resume_text_lower
    )

    experience = int(exp_match.group(1)) if exp_match else 0

    # Age extraction
    age = None

    age_match = re.search(
        r'age\s*[:\-]?\s*(\d+)',
        resume_text_lower
    )

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

    # Extract only important JD skills
    jd_skills = (
        " ".join(jd_info['primary_skills']) + " " +
        " ".join(jd_info['secondary_skills'])
    )

    # Clean resume text
    resume_clean = " ".join(resume_text.lower().split())

    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(
        stop_words='english',
        lowercase=True,
        ngram_range=(1, 2)
    )

    # Convert to vectors
    vectors = vectorizer.fit_transform([
        resume_clean,
        jd_skills
    ])

    # Cosine similarity
    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    # Convert to percentage
    score = round(similarity * 100, 2)

    # Extract matched skills
    resume_words = set(resume_clean.split())

    jd_words = set(jd_skills.split())

    matched = list(resume_words.intersection(jd_words))

    # Filter unnecessary words
    filtered_matched = [
        word for word in matched
        if len(word) > 2
    ]

    # Bonus scoring for exact skill matches
    bonus = len(filtered_matched) * 3

    score += bonus

    # Limit max score
    if score > 100:
        score = 100

    return round(score, 2), filtered_matched[:15]

