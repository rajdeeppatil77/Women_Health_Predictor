import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Synthetic Dataset Creation
def create_synthetic_data():
    # Symptoms: 1 = Yes, 0 = No
    
    data = {
        # Original Symptoms
        'fatigue': [], 'irregular_periods': [], 'weight_gain': [], 'hair_loss': [],
        'excess_hair_growth': [], 'mood_swings': [], 'pelvic_pain': [], 'lump_in_breast': [],
        'frequent_urination': [], 'thirst': [],
        
        # New Symptoms
        'nausea': [], 'missed_period': [], 'unexplained_weight_loss': [], 'recurring_fever': [],
        'swollen_lymph_nodes': [], 'burning_urination': [], 'cloudy_urine': [], 'abnormal_bleeding': [],
        'vaginal_itching': [], 'abnormal_discharge': [], 'fishy_odor': [], 'hot_flashes': [],
        'night_sweats': [], 'swelling_legs': [], 'severe_headache': [], 'bone_pain': [],
        'muscle_weakness': [], 'nipple_discharge': [], 'high_bp': [],
        
        'disease': []
    }
    
    # Generate 2000 samples for better coverage
    for _ in range(2000):
        # Randomize symptoms
        row = {k: np.random.choice([0, 1], p=[0.85, 0.15]) for k in data.keys() if k != 'disease'}
        
        # Enforce Logic for labelling (to create structured data)
        disease = "Healthy"
        
        # Prioritize serious/specific conditions
        if row['lump_in_breast'] or row['nipple_discharge']:
            disease = "Breast Cancer Risk"
        elif row['missed_period'] and row['nausea']:
            disease = "Possible Pregnancy"
        elif row['unexplained_weight_loss'] and row['recurring_fever'] and row['swollen_lymph_nodes']:
            disease = "Risk of HIV/AIDS"
        elif row['burning_urination'] and row['frequent_urination']:
            disease = "Urinary Tract Infection (UTI)"
        elif row['pelvic_pain'] and row['irregular_periods'] and row['abnormal_bleeding']:
            disease = "Cervical Cancer Risk"
        elif row['vaginal_itching'] and row['abnormal_discharge'] and not row['fishy_odor']:
            disease = "Vaginal Yeast Infection"
        elif row['abnormal_discharge'] and row['fishy_odor']:
            disease = "Bacterial Vaginosis"
        elif row['severe_headache'] and row['swelling_legs'] and row['high_bp']:
            disease = "Preeclampsia"
        elif row['hot_flashes'] and row['night_sweats']:
            disease = "Menopause Symptoms"
        elif row['bone_pain'] and row['muscle_weakness']:
            disease = "Vitamin D / Calcium Deficiency"
        elif row['bone_pain']:
            disease = "Osteoporosis Risk"
        elif row['recurring_fever'] and row['pelvic_pain'] and row['abnormal_discharge']:
            disease = "Pelvic Inflammatory Disease (PID)"
        elif row['irregular_periods'] and row['excess_hair_growth'] and row['weight_gain']:
            disease = "PCOS"
        elif row['fatigue'] and row['hair_loss'] and row['weight_gain']:
            disease = "Thyroid Disorder"
        elif row['frequent_urination'] and row['thirst']:
            disease = "Diabetes"
        elif row['fatigue'] and row['mood_swings']:
            disease = "Anemia"
            
        # Append to data
        for k in row:
            data[k].append(row[k])
        data['disease'].append(disease)
        
    return pd.DataFrame(data)

def train_model():
    print("Generating synthetic dataset...")
    df = create_synthetic_data()
    
    # Save dataset as requested
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
