# app/features.py

def extract_features(email):
    # safely handle missing or wrong data types
    subject = email.get("subject", "")
    if not isinstance(subject, str):
        subject = str(subject)

    body = email.get("body", "")
    if not isinstance(body, str):
        body = str(body)

    urls = email.get("urls", [])
    if not isinstance(urls, list):
        urls = []

    to_field = email.get("to", "")
    if not isinstance(to_field, str):
        to_field = str(to_field)

    features = {
        "subject_length": len(subject),
        "body_length": len(body),
        "num_urls": len(urls),
        "num_recipients": len(to_field.split(",")) if to_field else 0,
        "has_login": int("login" in body.lower() or "login" in subject.lower()),
        "has_verify": int("verify" in body.lower() or "verify" in subject.lower()),
    }
    return features

