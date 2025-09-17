# test_features.py
from app.features import extract_features
import json

print('Reading:', r'data\\processed\\sample.json')
feats = extract_features(r'data\\processed\\sample.json')
print('Features:')
print(json.dumps(feats, ensure_ascii=False, indent=2))
