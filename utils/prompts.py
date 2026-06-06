#Define all prompt templates

def resume_review_prompt(resume_text):
    return f"""You are an expert career coach. Review this resume and provide:
    1. Strengths
    2. Weaknesses
    3. Specific improvements
    4. ATS optimization tips
    
    Resume:
    {resume_text}"""

def interview_prep_prompt(job_role):
    return f"""Generate 10 interview questions for a {job_role} role with:
    - Expected answers
    - Tips for each question
    - Common mistakes to avoid"""

def roadmap_prompt(goal):
    return f"""Create a detailed career roadmap for someone wanting to become a {goal}:
    - Month-by-month plan
    - Skills to learn
    - Projects to build
    - Resources (free + paid)"""

def job_description_prompt(jd_text, resume_text):
    return f"""Analyze this job description against the resume:
    
    JD: {jd_text}
    Resume: {resume_text}
    
    Provide: match %, missing skills, suggestions to tailor the resume."""