import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from parser import parse_resume  # Import your resume parsing function

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Define the folder to store uploaded resumes
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'resumes')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# In-memory store for parsed resumes
parsed_resumes = []

def aggregate_skills():
    """
    Aggregate skill counts from all parsed resumes.
    Returns a dictionary of skill names and their frequency.
    """
    skill_count = {}
    for resume in parsed_resumes:
        skills = resume.get('Skills', '')
        for skill in skills.split(','):
            skill = skill.strip()
            if skill:
                skill_count[skill] = skill_count.get(skill, 0) + 1
    return skill_count

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Check if the file part is present in the request
        if 'resume' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['resume']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Save the uploaded file in the UPLOAD_FOLDER
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # Parse the resume and store the result
            result = parse_resume(filepath)
            parsed_resumes.append(result)
    
    # Aggregate skills from all parsed resumes for data visualization
    skills_data = aggregate_skills()
    skills_labels = list(skills_data.keys())
    skills_values = list(skills_data.values())
    
    # Render the index.html template with parsed resume and aggregated skill data
    return render_template('index.html',
                           result=result,
                           skills_labels=json.dumps(skills_labels),
                           skills_values=json.dumps(skills_values))

if __name__ == '__main__':
    app.run(debug=True)
