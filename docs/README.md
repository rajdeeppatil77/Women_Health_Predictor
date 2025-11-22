# Women Health Predictor

## Overview
The **Women Health Predictor** is a web application designed to empower tribal women with accessible health insights. It uses Machine Learning to predict potential health issues based on symptoms and provides guidance, emergency contacts, and a health chatbot.

## Features
- **Disease Prediction**: AI-based analysis of symptoms (PCOS, Thyroid, Diabetes, etc.).
- **Interactive Dashboard**: Track health history.
- **Chatbot Assistant**: Answer health-related queries.
- **Emergency Support**: One-click access to ambulance and helplines.
- **Simple UI**: Designed for ease of use with visual icons.

## Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript
- **ML Model**: Scikit-learn (Random Forest)
- **Database**: SQLite (via SQLAlchemy - *Planned*)

## Installation & Setup

### Prerequisites
- Python 3.8 or higher

### Steps
1.  **Clone the repository** (or extract the project folder).
2.  **Navigate to the project directory**:
    ```bash
    cd Women_Health_Predictor_project
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r backend/requirements.txt
    ```
4.  **Run the Application**:
    ```bash
    python backend/app.py
    ```
5.  **Open in Browser**:
    Visit `http://localhost:5000`

## Folder Structure
```
Women_Health_Predictor_project/
├── backend/
│   ├── app.py              # Main Flask Application
│   ├── train_model.py      # ML Model Training Script
│   ├── disease_model.pkl   # Trained ML Model
│   ├── requirements.txt    # Python Dependencies
│   ├── static/             # CSS, JS, Images
│   └── templates/          # HTML Templates
└── docs/                   # Project Documentation
```
