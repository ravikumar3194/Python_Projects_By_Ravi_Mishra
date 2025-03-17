🚀 Automated Threat Hunting Dashboard
Created by Ravi Kumar Mishra

📌 Project Overview
The Automated Threat Hunting Dashboard is a Streamlit-based web application that allows users to:
✅ Upload log files in CSV format
✅ View raw log data in a structured format
✅ Highlight severity levels dynamically
✅ Detect potential threats based on predefined rules

🖼️ Project Demo
(Replace with actual image path)

📂 Project Structure
graphql
Copy
Edit
AUTOMATED_THREAT_HUNTING/
│── dashboard/
│   ├── templates/
│   │   ├── index.html  # HTML for frontend (if applicable)
│   ├── app.py          # Streamlit app main script
│── data/
│   ├── demo_data.csv     # Sample log data
│── models/
│   ├── anomaly_model.pkl  # Machine learning model for anomaly detection
│   ├── label_encoder.pkl  # Label encoder for categorical data
│── scripts/
│   ├── preprocess_logs.py  # Log preprocessing functions
│── requirements.txt  # Python dependencies
│── README.md  # Project documentation
🚀 Features
🔹 CSV Upload: Users can upload log files via the dashboard.
🔹 Data Preview: Displays raw logs in a tabular format.
🔹 Severity Highlighting: Logs are color-coded based on severity levels (Low, Medium, High, Critical).
🔹 Anomaly Detection (Optional): Uses a trained model to detect anomalies in log data.
🔹 User-Friendly UI: Built with Streamlit for an interactive experience.

🛠️ Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Ravi-Mishra2330/Automated-Threat-Hunting.git
cd Automated-Threat-Hunting
2️⃣ Set Up a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
streamlit run dashboard/app.py
The app will start and open in your browser at http://localhost:8501

📌 Example Log File Format
timestamp	event	severity	source_ip	destination_ip
2025-03-17 12:00:01	Login Attempt	Low	192.168.1.10	10.0.0.5
2025-03-17 12:05:32	Failed Login	Medium	192.168.1.15	10.0.0.5
2025-03-17 12:10:45	Malware Detected	High	172.16.0.12	10.0.0.8
2025-03-17 12:15:23	Port Scan	Critical	192.168.1.20	10.0.0.9
🎯 Future Enhancements
📌 Live Log Monitoring – Integrate real-time log ingestion.
📌 Database Integration – Store and retrieve historical logs.
📌 Threat Scoring System – Assign risk scores to threats.
📌 Email Alerts – Notify security teams about critical anomalies.

🤝 Contributing
Feel free to fork the repo, make improvements, and submit a PR!

📜 License
This project is licensed under the MIT License.

