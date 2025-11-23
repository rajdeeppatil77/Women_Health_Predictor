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
    
    # New Symptoms (Extended)
    nausea = data.get('nausea', 0)
    missed_period = data.get('missed_period', 0)
    unexplained_weight_loss = data.get('unexplained_weight_loss', 0)
    recurring_fever = data.get('recurring_fever', 0)
    swollen_lymph_nodes = data.get('swollen_lymph_nodes', 0)
    burning_urination = data.get('burning_urination', 0)
    cloudy_urine = data.get('cloudy_urine', 0)
    abnormal_bleeding = data.get('abnormal_bleeding', 0)
    vaginal_itching = data.get('vaginal_itching', 0)
    abnormal_discharge = data.get('abnormal_discharge', 0)
    fishy_odor = data.get('fishy_odor', 0)
    hot_flashes = data.get('hot_flashes', 0)
    night_sweats = data.get('night_sweats', 0)
    swelling_legs = data.get('swelling_legs', 0)
    severe_headache = data.get('severe_headache', 0)
    bone_pain = data.get('bone_pain', 0)
    muscle_weakness = data.get('muscle_weakness', 0)
    nipple_discharge = data.get('nipple_discharge', 0)
    high_bp = data.get('high_bp', 0)

    # New Symptoms (Tribal Health Expansion)
    high_fever = data.get('high_fever', 0)
    persistent_cough = data.get('persistent_cough', 0)
    blood_in_sputum = data.get('blood_in_sputum', 0)
    severe_joint_pain = data.get('severe_joint_pain', 0)
    stomach_pain_fever = data.get('stomach_pain_fever', 0)
    difficulty_conceiving = data.get('difficulty_conceiving', 0)
    genital_warts = data.get('genital_warts', 0)
    is_pregnant = data.get('is_pregnant', 0)
    gestational_diabetes_symptoms = data.get('gestational_diabetes_symptoms', 0)
    maternal_sepsis_symptoms = data.get('maternal_sepsis_symptoms', 0)
    numbness_tingling = data.get('numbness_tingling', 0)
    pale_skin = data.get('pale_skin', 0)
    neck_swelling = data.get('neck_swelling', 0)
    brittle_nails = data.get('brittle_nails', 0)
    persistent_sadness = data.get('persistent_sadness', 0)
    anxiety_panic = data.get('anxiety_panic', 0)
    postpartum_sadness = data.get('postpartum_sadness', 0)

    # Prediction Logic
    prediction = "Healthy"
    
    # --- Infectious Diseases ---
    if persistent_cough and blood_in_sputum:
        prediction = "Tuberculosis (TB) Risk"
    elif high_fever and severe_joint_pain:
        prediction = "Dengue Fever Risk"
    elif high_fever and stomach_pain_fever:
        prediction = "Typhoid Fever Risk"
    elif high_fever and recurring_fever: # Malaria often has recurring fever
        prediction = "Malaria Risk"
    elif burning_urination and frequent_urination:
        prediction = "Urinary Tract Infection (UTI)"
    elif recurring_fever and pelvic_pain and abnormal_discharge:
        prediction = "Pelvic Inflammatory Disease (PID)"
    elif vaginal_itching and abnormal_discharge and not fishy_odor:
        prediction = "Vaginal Yeast Infection"
    elif abnormal_discharge and fishy_odor:
        prediction = "Bacterial Vaginosis"
    elif unexplained_weight_loss and recurring_fever and swollen_lymph_nodes:
        prediction = "Risk of HIV/AIDS"

    # --- Maternal Health ---
    elif is_pregnant and severe_headache and swelling_legs and high_bp:
        prediction = "Preeclampsia (High Risk Pregnancy)"
    elif is_pregnant and gestational_diabetes_symptoms:
        prediction = "Gestational Diabetes"
    elif maternal_sepsis_symptoms:
        prediction = "Maternal Sepsis (Emergency)"
    elif missed_period and nausea and fatigue:
        prediction = "Possible Pregnancy"

    # --- Reproductive & Gynecological ---
    elif lump_in_breast or nipple_discharge:
        prediction = "Breast Cancer Risk (Consult Doctor)"
    elif pelvic_pain and irregular_periods and abnormal_bleeding:
        prediction = "Cervical Cancer Risk"
    elif genital_warts:
        prediction = "HPV Infection Risk"
    elif difficulty_conceiving:
        prediction = "Infertility Risk (Consult Doctor)"
    elif pelvic_pain and irregular_periods: 
        prediction = "Endometriosis Risk"
    elif irregular_periods and excess_hair_growth and weight_gain:
        prediction = "PCOS"
    elif hot_flashes and night_sweats and irregular_periods:
        prediction = "Menopause Symptoms"

    # --- Nutritional Deficiencies ---
    elif neck_swelling:
        prediction = "Iodine Deficiency (Goiter)"
    elif numbness_tingling and fatigue:
        prediction = "Vitamin B12 Deficiency"
    elif pale_skin and fatigue:
        prediction = "Folate Deficiency / Anemia"
    elif bone_pain and muscle_weakness:
        prediction = "Vitamin D / Calcium Deficiency"
    elif brittle_nails and hair_loss:
        prediction = "Protein Deficiency"
    elif bone_pain:
        prediction = "Osteoporosis Risk"
    elif fatigue and mood_swings and irregular_periods:
        prediction = "Anemia"

    # --- Mental Health ---
    elif postpartum_sadness:
        prediction = "Postpartum Depression"
    elif persistent_sadness:
        prediction = "Depression"
    elif anxiety_panic:
        prediction = "Anxiety Disorder"
        
    # --- Chronic/Other ---
    elif fatigue and hair_loss and weight_gain:
        prediction = "Thyroid Disorder"
    elif frequent_urination and thirst and fatigue:
        prediction = "Diabetes"

    # Recommendations
    recommendations = {
        "Healthy": "Keep up the good lifestyle! Regular checkups are still recommended.",
        "PCOS": "Consult a gynecologist. Maintain a healthy diet and exercise.",
        "Thyroid Disorder": "Consult an endocrinologist. Get TSH levels checked.",
        "Diabetes": "Consult a general physician. Monitor sugar levels.",
        "Anemia": "Increase iron intake (Spinach, Beetroot, Jaggery). Consult a doctor.",
        "Breast Cancer Risk (Consult Doctor)": "IMMEDIATE ACTION: Please visit a specialist for a mammogram.",
        "Possible Pregnancy": "Take a home pregnancy test or visit a clinic for confirmation.",
        "Risk of HIV/AIDS": "Please visit a testing center immediately for a blood test. Early detection is key.",
        "Urinary Tract Infection (UTI)": "Drink plenty of water and consult a doctor for antibiotics.",
        "Endometriosis Risk": "Consult a gynecologist for a pelvic exam and ultrasound.",
        "Cervical Cancer Risk": "IMMEDIATE ACTION: Consult a gynecologist for a Pap smear test.",
        "Vaginal Yeast Infection": "Consult a doctor for antifungal medication.",
        "Bacterial Vaginosis": "Consult a gynecologist for antibiotics.",
        "Preeclampsia (High Risk Pregnancy)": "EMERGENCY: Visit a hospital immediately. High BP in pregnancy is dangerous.",
        "Menopause Symptoms": "Consult a doctor for management strategies if symptoms are severe.",
        "Vitamin D / Calcium Deficiency": "Consult a doctor for supplements and bone density test.",
        "Osteoporosis Risk": "Consult an orthopedist for a bone density test.",
        "Pelvic Inflammatory Disease (PID)": "Consult a gynecologist immediately to prevent complications.",
        
        # Tribal Health Specific Recommendations
        "Tuberculosis (TB) Risk": "IMMEDIATE ACTION: Visit a government hospital for a free TB test. It is curable.",
        "Dengue Fever Risk": "Rest, drink plenty of fluids, and visit a doctor immediately. Do not take aspirin.",
        "Typhoid Fever Risk": "Consult a doctor for antibiotics. Drink only boiled or treated water.",
        "Malaria Risk": "Visit a health center for a blood test. Use mosquito nets.",
        "HPV Infection Risk": "Consult a gynecologist. Ask about the HPV vaccine.",
        "Infertility Risk (Consult Doctor)": "Consult a fertility specialist for evaluation.",
        "Gestational Diabetes": "Monitor blood sugar. Follow a strict diet plan advised by a doctor.",
        "Maternal Sepsis (Emergency)": "EMERGENCY: Go to the nearest hospital immediately. This is life-threatening.",
        "Iodine Deficiency (Goiter)": "Use iodized salt in your cooking. Consult a doctor.",
        "Vitamin B12 Deficiency": "Eat more dairy, eggs, or fortified foods. Consult a doctor for supplements.",
        "Folate Deficiency / Anemia": "Eat green leafy vegetables, beans, and lentils. Take iron/folic acid tablets.",
        "Protein Deficiency": "Increase intake of pulses (dal), eggs, milk, and nuts.",
        "Postpartum Depression": "Talk to a health worker or counselor. You are not alone; support is available.",
        "Depression": "Seek help from a mental health professional or counselor.",
        "Anxiety Disorder": "Practice deep breathing. Consult a doctor if it affects daily life."
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
