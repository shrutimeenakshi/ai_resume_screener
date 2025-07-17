def seed_roles():
    from app import db, JobRole

    default_roles = [
        {
            'role_key': 'python_dev',
            'role_name': 'Python Developer',
            'job_description': 'Should know Python, Flask, SQL, APIs, Git.'
        },
        {
            'role_key': 'frontend_dev',
            'role_name': 'Frontend Developer',
            'job_description': 'Should know HTML, CSS, JavaScript, React.'
        },
        {
            'role_key': 'data_scientist',
            'role_name': 'Data Scientist',
            'job_description': 'Should know Python, Pandas, Scikit-learn, and ML algorithms.'
        },
        {
            'role_key': 'backend_dev',
            'role_name': 'Backend Developer',
            'job_description': 'Should know Python, Django/Flask, REST APIs, and databases.'
        },
        {
            'role_key': 'fullstack_dev',
            'role_name': 'Fullstack Developer',
            'job_description': 'Should know frontend + backend tech (React, Flask, SQL, APIs).'
        },
        {
            'role_key': 'ai_engineer',
            'role_name': 'AI Engineer',
            'job_description': 'Should know AI/ML concepts, Python, TensorFlow/PyTorch.'
        },
        {
            'role_key': 'cybersecurity_analyst',
            'role_name': 'Cybersecurity Analyst',
            'job_description': 'Should understand network security, tools like Wireshark, Nmap.'
        },
        {
            'role_key': 'devops_engineer',
            'role_name': 'DevOps Engineer',
            'job_description': 'Should know CI/CD, Docker, Kubernetes, and cloud platforms.'
        }
    ]

    for role in default_roles:
        existing = JobRole.query.filter_by(role_key=role['role_key']).first()
        if not existing:
            db.session.add(JobRole(**role))
    db.session.commit()
    print("✅ Done! Inserted 8 new roles.")

