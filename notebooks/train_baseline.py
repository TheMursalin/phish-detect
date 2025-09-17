import json
import sys, os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# make sure Python can find the app folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.features import extract_features

print("Loading dataset...")

X, y = [], []

with open("data/processed/train.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        j = json.loads(line.strip())
        feats = extract_features(j)
        X.append(list(feats.values()))
        y.append(j["label"])

print(f"Loaded {len(X)} samples")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y if len(set(y)) > 1 else None, random_state=42
)

print("Training model...")
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

print("Evaluating...")
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/phish_model.pkl")
print("Model saved to models/phish_model.pkl")
