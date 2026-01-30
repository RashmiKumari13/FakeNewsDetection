import joblib
import os
from src.preprocessing import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(BASE_DIR, "models/classifier.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "models/tfidf_vector.pkl"))

def predict_news(text):
    text = clean_text(text)
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return "REAL NEWS 🟢" if prediction == 1 else "FAKE NEWS 🔴"
