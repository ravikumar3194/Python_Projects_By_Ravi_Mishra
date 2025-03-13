import re
import pdfminer.high_level
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract raw text from a PDF file."""
    return pdfminer.high_level.extract_text(pdf_path)

def extract_email(text):
    """Extract email from text using regex."""
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else None

def extract_phone_number(text):
    """Extract phone number including optional country code."""
    pattern = r"(?:\+\d{1,3}[-.\s]?)?\d{10}\b"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_name(text):
    """
    Heuristic approach:
    - Check first few lines for uppercase or title case text.
    - Fallback to spaCy NER for PERSON entities.
    """
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    
    # Check first 5 lines for uppercase or title case
    candidate_names = []
    for line in lines[:5]:
        if (line.isupper() or line.istitle()) and len(line) > 2:
            candidate_names.append(line)
    
    if candidate_names:
        return max(candidate_names, key=len)
    
    # Fallback to spaCy NER
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    """Extract predefined skills."""
    skills_list = [
        "Python", "Machine Learning", "Flask", "Django", "SQL", "AWS", 
        "Azure", "Excel", "Oracle", "Shell Scripting", "C++", "Java"
    ]
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return ", ".join(found_skills)

def extract_education(text):
    """
    Naive approach to find lines containing education keywords.
    You can improve this logic or use advanced NLP for better accuracy.
    """
    education_keywords = ["btech", "bachelor", "master", "university", "college", "institute", "degree"]
    lines = text.split('\n')
    edu_lines = []
    for line in lines:
        if any(keyword in line.lower() for keyword in education_keywords):
            edu_lines.append(line.strip())
    return " | ".join(edu_lines) if edu_lines else None

def extract_experience(text):
    """
    Simple approach to find lines mentioning 'experience' or job positions.
    Again, can be enhanced with NLP or specific patterns (dates, roles, etc.).
    """
    exp_keywords = ["experience", "worked at", "intern", "engineer", "developer"]
    lines = text.split('\n')
    exp_lines = []
    for line in lines:
        if any(keyword in line.lower() for keyword in exp_keywords):
            exp_lines.append(line.strip())
    return " | ".join(exp_lines) if exp_lines else None

def extract_certifications(text):
    """
    Look for lines mentioning certifications, e.g., 'Certification', 'Certified', 'AWS Certified'.
    """
    cert_keywords = ["certification", "certified", "aws-certified", "az-900", "az-104"]
    lines = text.split('\n')
    cert_lines = []
    for line in lines:
        if any(keyword in line.lower() for keyword in cert_keywords):
            cert_lines.append(line.strip())
    return " | ".join(cert_lines) if cert_lines else None

def parse_resume(pdf_path):
    """Main function to parse resume and return a dictionary of extracted data."""
    text = extract_text_from_pdf(pdf_path)
    
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone_number(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Experience": extract_experience(text),
        "Certifications": extract_certifications(text)
    }

if __name__ == "__main__":
    sample_path = "resumes/Ravi_Kumar_Mishra_Resume_2025.pdf"
    parsed = parse_resume(sample_path)
    print(parsed)
