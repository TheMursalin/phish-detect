import json
import joblib
from app.features import extract_features

# Load trained model
clf = joblib.load("models/phish_model.pkl")

# Example new email
email_file = "data/processed/sample.json"
with open(email_file, "r", encoding="utf-8-sig") as f:
    email_data = json.load(f)

# Extract features
features = extract_features(email_data)
X = [list(features.values())]

# Predict
prediction = clf.predict(X)
print("Phishing" if prediction[0] == 1 else "Legitimate")
