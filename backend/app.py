from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Lightweight Logic for Vercel Demo (Removes heavy ML dependencies)
@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Extract features
    fatigue = data.get('fatigue', 0)
    irregular_periods = data.get('irregular_periods', 0)
    weight_gain = data.get('weight_gain', 0)
    hair_loss = data.get('hair_loss', 0)
    excess_hair_growth = data.get('excess_hair_growth', 0)
    mood_swings = data.get('mood_swings', 0)
    pelvic_pain = data.get('pelvic_pain', 0)
    lump_in_breast = data.get('lump_in_breast', 0)
    frequent_urination = data.get('frequent_urination', 0)
    thirst = data.get('thirst', 0)

    # Prediction Logic (Matches the logic used to train the model)
    prediction = "Healthy"
    
    if lump_in_breast:
        prediction = "Breast Cancer Risk (Consult Doctor)"
    elif irregular_periods and excess_hair_growth and weight_gain:
        prediction = "PCOS"
    elif fatigue and hair_loss and weight_gain:
        prediction = "Thyroid Disorder"
    elif frequent_urination and thirst and fatigue:
        prediction = "Diabetes"
    elif fatigue and mood_swings and irregular_periods:
        prediction = "Anemia"

    # Recommendations
    recommendations = {
        "Healthy": "Keep up the good lifestyle! Regular checkups are still recommended.",
        "PCOS": "Consult a gynecologist. Maintain a healthy diet and exercise.",
        "Thyroid Disorder": "Consult an endocrinologist. Get TSH levels checked.",
        "Diabetes": "Consult a general physician. Monitor sugar levels.",
        "Anemia": "Increase iron intake (Spinach, Beetroot). Consult a doctor.",
        "Breast Cancer Risk (Consult Doctor)": "IMMEDIATE ACTION: Please visit a specialist for a mammogram."
    }
    
    return jsonify({
        'prediction': prediction,
        'recommendation': recommendations.get(prediction, "Consult a doctor.")
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    # Simple rule-based chatbot for demo
    user_msg = request.json.get('message', '').lower()
    
    if 'period' in user_msg:
        response = "Irregular periods can be caused by stress, PCOS, or thyroid issues. If it persists, see a doctor."
    elif 'pain' in user_msg:
        response = "Pain can be a sign of many things. If it's severe pelvic pain, it could be endometriosis or infection."
    elif 'diet' in user_msg:
        response = "A balanced diet with iron, calcium, and protein is essential for women's health."
    elif 'hello' in user_msg or 'hi' in user_msg:
        response = "Namaste! How can I help you with your health today?"
    else:
        response = "I am a simple AI. Please ask about symptoms, diet, or specific conditions."
        
    return jsonify({'response': response})

@app.route('/api/emergency', methods=['GET'])
def emergency():
    contacts = [
        {"name": "Ambulance", "number": "102"},
        {"name": "Women Helpline", "number": "1091"},
        {"name": "Pregnancy Support", "number": "104"},
        {"name": "Local Asha Worker", "number": "+91-9876543210"}
    ]
    return jsonify(contacts)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

@app.route('/dashboard_page')
def dashboard_page():
    return render_template('dashboard.html')

@app.route('/chat_page')
def chat_page():
    return render_template('chat.html')

@app.route('/emergency_page')
def emergency_page():
    return render_template('emergency.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
