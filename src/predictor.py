import joblib
import os
# Import the cleaner from the same directory
from preprocessing import clean_text_fast 

# Get the path to the 'models' folder (one level up from 'src')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models")

# Load model and vectorizer
vectorizer = joblib.load(os.path.join(MODEL_PATH, "tfidf_vector.pkl"))
model = joblib.load(os.path.join(MODEL_PATH, "classifier.pkl"))

def predict_news(text):
    text = clean_text_fast(text)
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    # Adjust 1/0 based on how your model was trained
    return "REAL NEWS 🟢" if prediction == 1 else "FAKE NEWS 🔴"