# 🔐 VREP: Vendor Risk Evaluation Portal

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A cybersecurity assessment system for evaluating cloud service vendors using automated risk analysis and prevention suggestions.

---

## 📚 Table of Contents

- [📘 About](#-about)
- [🚀 Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [📂 Project Structure](#-project-structure)
- [📦 Setup Instructions](#-setup-instructions)
- [🖼️ Screenshots](#-screenshots)
- [🔮 Future Enhancements](#-future-enhancements)
- [📄 License](#-license)

---

## 📘 About

**VREP** is a web portal that allows employees to submit cloud vendor documents, automatically assess risk scores using custom logic, and display results on an admin dashboard. It includes detailed explanations for each risk level and provides suggested prevention strategies.

---

## 🚀 Features

| Module                       | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| 📄 Vendor Submission         | Uploads vendor details and JSON configuration files                        |
| 📈 Risk Scoring Engine       | Parses uploaded files and computes a risk score (0–100)                     |
| ⚠️ Risk Level Breakdown       | Provides Risk Level, Description, and Prevention Tips                      |
| 🧑‍💼 Admin Dashboard          | Approve/Reject vendors with comments                                       |
| 🔏 Digital Signature Check   | (Optional) Verifies vendor file authenticity using RSA                    |
| 🔐 Secure Uploads            | All files are saved in `/static/uploads`                                   |
| 📊 SQLite + SQLAlchemy       | Persistent vendor submission and scoring data                              |

---

## 🛠️ Technologies Used

- Python 3.10
- Flask
- Jinja2 Templates
- SQLAlchemy (SQLite)
- HTML5/CSS3/JavaScript
- Bootstrap (for styling)
- RSA (for signature validation, optional)

---

## 📂 Project Structure

VREP/
├── app.py 
├── models.py 
├── risk_engine.py 
├── config.py # Flask configurations
├── vendors.db # SQLite DB file
├── static/
│ ├── style.css # Custom CSS
│ ├── script.js # JS logic
│ └── uploads/
├── templates/
│ ├── index.html 
│ ├── dashboard.html 
│ └── login.html # (optional) 
├── requirements.txt 


---

## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/VREP.git
   cd VREP

## Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install Dependencies

pip install -r requirements.txt


## Run the App

python app.py

## Access the Portal

http://127.0.0.1:5000/
