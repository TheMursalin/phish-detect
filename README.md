# 🛡️ Phish-Detect

A machine learning project for detecting **phishing emails** using Python, scikit-learn, and feature engineering.  
It extracts meaningful features from emails (like subject length, link count, suspicious URLs) and trains a Random Forest classifier to classify emails as **legit** or **phishing**.

---

## 📌 Features
- Extracts text-based and URL-based features from emails  
- Supports JSONL datasets for training  
- Random Forest classifier for robust detection  
- Includes training and testing scripts  
- Easy to extend with more features or models  

---

## 🚀 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/TheMursalin/phish-detect.git
cd phish-detect
pip install -r requirements.txt
