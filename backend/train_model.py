import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Synthetic Dataset Creation
def create_synthetic_data():
    # Symptoms: 1 = Yes, 0 = No
    # Diseases: Anemia, PCOS, Thyroid, Breast Cancer Risk, Diabetes
    
    data = {
        'fatigue': [],
        'irregular_periods': [],
        'weight_gain': [],
        'hair_loss': [],
        'excess_hair_growth': [],
        'mood_swings': [],
        'pelvic_pain': [],
        'lump_in_breast': [],
        'frequent_urination': [],
        'thirst': [],
        'disease': []
    }
    
    # Generate 1000 samples
    for _ in range(1000):
        # Random symptoms
        fatigue = np.random.choice([0, 1])
        irregular_periods = np.random.choice([0, 1])
        weight_gain = np.random.choice([0, 1])
        hair_loss = np.random.choice([0, 1])
        excess_hair_growth = np.random.choice([0, 1])
        mood_swings = np.random.choice([0, 1])
        pelvic_pain = np.random.choice([0, 1])
        lump_in_breast = np.random.choice([0, 1], p=[0.95, 0.05]) # Rare
        frequent_urination = np.random.choice([0, 1])
        thirst = np.random.choice([0, 1])
        
        # Logic for labelling (Simplified for demo)
        disease = "Healthy"
        
        if lump_in_breast:
            disease = "Breast Cancer Risk (Consult Doctor)"
        elif irregular_periods and excess_hair_growth and weight_gain:
            disease = "PCOS"
        elif fatigue and hair_loss and weight_gain:
            disease = "Thyroid Disorder"
        elif frequent_urination and thirst and fatigue:
            disease = "Diabetes"
        elif fatigue and mood_swings and irregular_periods:
            disease = "Anemia"
            
        data['fatigue'].append(fatigue)
        data['irregular_periods'].append(irregular_periods)
        data['weight_gain'].append(weight_gain)
        data['hair_loss'].append(hair_loss)
        data['excess_hair_growth'].append(excess_hair_growth)
        data['mood_swings'].append(mood_swings)
        data['pelvic_pain'].append(pelvic_pain)
        data['lump_in_breast'].append(lump_in_breast)
        data['frequent_urination'].append(frequent_urination)
        data['thirst'].append(thirst)
        data['disease'].append(disease)
        
    return pd.DataFrame(data)

def train_model():
    df = create_synthetic_data()
    X = df.drop('disease', axis=1)
    y = df['disease']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    joblib.dump(model, 'disease_model.pkl')
    print("Model saved to disease_model.pkl")

if __name__ == "__main__":
    train_model()
