Automated Resume Parser & Analyzer
An automated web application built with Python, Flask, and Bootstrap that extracts key details from resumes (PDFs) such as Name, Email, Phone, Skills, Education, Experience, and Certifications. It also aggregates data across multiple resumes and visualizes skills distribution using Chart.js.

Features
Resume Parsing:
Automatically extract details like Name, Email, Phone, Skills, Education, Experience, and Certifications from uploaded PDF resumes using pdfminer.six, spacy, and regular expressions.

Interactive Dashboard:
A modern, responsive UI built with Flask and Bootstrap featuring:

A polished landing page with a navbar and hero section.
A Bootstrap-styled file upload form.
A results dashboard displaying parsed details in a card layout with a modal for full JSON details.
An interactive Chart.js bar chart visualizing aggregated skills from all parsed resumes.
A consistent footer with social media links.
Data Visualization:
Aggregate skills data across multiple resumes and display interactive charts.

Technologies Used
Backend: Python, Flask, pdfminer.six, spacy, pandas
Frontend: Bootstrap 4, Chart.js, Font Awesome
Deployment: (Optional) Gunicorn for production deployments
Demo

Installation
Clone the Repository:

bash
Copy
Edit
git clone "https://github.com/ravikumar3194/Python_Projects_By_Ravi_Mishra.git"
cd Python_Projects_By_Ravi_Mishra/Resume_Parser
Create a Virtual Environment and Activate It:

bash
Copy
Edit
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install the Requirements:

bash
Copy
Edit
pip install -r requirements.txt
Download the spaCy English Model:

bash
Copy
Edit
python -m spacy download en_core_web_sm
Usage
Run the Flask Application:

bash
Copy
Edit
python app.py
Access the App:

Open your browser and navigate to http://127.0.0.1:5000.

Upload a Resume:

Use the file upload form to submit a PDF resume. The app will parse the resume, display the extracted details, and update the skills distribution chart.

Project Structure
php
Copy
Edit
Resume_Parser/
│
├── app.py              # Main Flask application
├── parser.py           # Resume parsing logic
├── requirements.txt    # Python dependencies
├── resumes/            # Folder for uploaded resumes
├── static/             # Static files (CSS, images, etc.)
│   └── styles.css      # Custom CSS styles
└── templates/          # HTML templates
    └── index.html      # Main page template
Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements, new features, or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Ravi Kumar Mishra

GitHub
LinkedIn
