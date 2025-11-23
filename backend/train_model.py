import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Synthetic Dataset Creation for Tribal Health
def create_synthetic_data():
    # Symptoms: 1 = Yes, 0 = No
    
    data = {
        # Original Symptoms
        'fatigue': [], 'irregular_periods': [], 'weight_gain': [], 'hair_loss': [],
        'excess_hair_growth': [], 'mood_swings': [], 'pelvic_pain': [], 'lump_in_breast': [],
        'frequent_urination': [], 'thirst': [],
        
        # Previous Expansion Symptoms
        'nausea': [], 'missed_period': [], 'unexplained_weight_loss': [], 'recurring_fever': [],
        'swollen_lymph_nodes': [], 'burning_urination': [], 'cloudy_urine': [], 'abnormal_bleeding': [],
        'vaginal_itching': [], 'abnormal_discharge': [], 'fishy_odor': [], 'hot_flashes': [],
        'night_sweats': [], 'swelling_legs': [], 'severe_headache': [], 'bone_pain': [],
        'muscle_weakness': [], 'nipple_discharge': [], 'high_bp': [],
        
        # Tribal Health Expansion Symptoms
        'high_fever': [], 'persistent_cough': [], 'blood_in_sputum': [], 'severe_joint_pain': [],
        'stomach_pain_fever': [], 'difficulty_conceiving': [], 'genital_warts': [], 'is_pregnant': [],
        'gestational_diabetes_symptoms': [], 'maternal_sepsis_symptoms': [], 'numbness_tingling': [],
        'pale_skin': [], 'neck_swelling': [], 'brittle_nails': [], 'persistent_sadness': [],
        'anxiety_panic': [], 'postpartum_sadness': [],
        
        'disease': []
    }
    
    # Generate 3000 samples for better coverage
    for _ in range(3000):
        # Randomize symptoms
        row = {k: np.random.choice([0, 1], p=[0.90, 0.10]) for k in data.keys() if k != 'disease'}
        
        # Enforce Logic for labelling (to create structured data)
        disease = "Healthy"
        
        # --- Infectious ---
        if row['persistent_cough'] and row['blood_in_sputum']:
            disease = "Tuberculosis (TB) Risk"
        elif row['high_fever'] and row['severe_joint_pain']:
            disease = "Dengue Fever Risk"
        elif row['high_fever'] and row['stomach_pain_fever']:
            disease = "Typhoid Fever Risk"
        elif row['high_fever'] and row['recurring_fever']:
            disease = "Malaria Risk"
        elif row['burning_urination'] and row['frequent_urination']:
            disease = "Urinary Tract Infection (UTI)"
        elif row['recurring_fever'] and row['pelvic_pain'] and row['abnormal_discharge']:
            disease = "Pelvic Inflammatory Disease (PID)"
        elif row['vaginal_itching'] and row['abnormal_discharge'] and not row['fishy_odor']:
            disease = "Vaginal Yeast Infection"
        elif row['abnormal_discharge'] and row['fishy_odor']:
            disease = "Bacterial Vaginosis"
        elif row['unexplained_weight_loss'] and row['recurring_fever'] and row['swollen_lymph_nodes']:
            disease = "Risk of HIV/AIDS"

        # --- Maternal ---
        elif row['is_pregnant'] and row['severe_headache'] and row['swelling_legs'] and row['high_bp']:
            disease = "Preeclampsia"
        elif row['is_pregnant'] and row['gestational_diabetes_symptoms']:
            disease = "Gestational Diabetes"
        elif row['maternal_sepsis_symptoms']:
            disease = "Maternal Sepsis"
        elif row['missed_period'] and row['nausea']:
            disease = "Possible Pregnancy"

        # --- Reproductive ---
        elif row['lump_in_breast'] or row['nipple_discharge']:
            disease = "Breast Cancer Risk"
        elif row['pelvic_pain'] and row['irregular_periods'] and row['abnormal_bleeding']:
            disease = "Cervical Cancer Risk"
        elif row['genital_warts']:
            disease = "HPV Infection Risk"
        elif row['difficulty_conceiving']:
            disease = "Infertility Risk"
        elif row['irregular_periods'] and row['excess_hair_growth'] and row['weight_gain']:
            disease = "PCOS"
        elif row['hot_flashes'] and row['night_sweats']:
            disease = "Menopause Symptoms"

        # --- Nutritional ---
        elif row['neck_swelling']:
            disease = "Iodine Deficiency"
        elif row['numbness_tingling'] and row['fatigue']:
            disease = "Vitamin B12 Deficiency"
        elif row['pale_skin'] and row['fatigue']:
            disease = "Folate Deficiency / Anemia"
        elif row['bone_pain'] and row['muscle_weakness']:
            disease = "Vitamin D / Calcium Deficiency"
        elif row['brittle_nails'] and row['hair_loss']:
            disease = "Protein Deficiency"
        elif row['bone_pain']:
            disease = "Osteoporosis Risk"
        elif row['fatigue'] and row['mood_swings']:
            disease = "Anemia"

        # --- Mental ---
        elif row['postpartum_sadness']:
            disease = "Postpartum Depression"
        elif row['persistent_sadness']:
            disease = "Depression"
        elif row['anxiety_panic']:
            disease = "Anxiety Disorder"
            
        # --- Chronic ---
        elif row['fatigue'] and row['hair_loss'] and row['weight_gain']:
            disease = "Thyroid Disorder"
        elif row['frequent_urination'] and row['thirst']:
            disease = "Diabetes"
            
        # Append to data
        for k in row:
            data[k].append(row[k])
        data['disease'].append(disease)
        
    return pd.DataFrame(data)

def train_model():
    print("Generating comprehensive tribal health dataset...")
    df = create_synthetic_data()
    
    # Save dataset
    df.to_csv('women_health_dataset.csv', index=False)
    print("Dataset saved to women_health_dataset.csv")
    
    X = df.drop('disease', axis=1)
    y = df['disease']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    joblib.dump(model, 'disease_model.pkl')
    print("Model saved to disease_model.pkl")

if __name__ == "__main__":
    train_model()
