# Fake News Detection using ML

## 📌 Overview
A Machine Learning–based Fake News Detection system that classifies news articles as FAKE or REAL using Natural Language Processing (NLP) techniques.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, Scikit-Learn, NLTK
- **Frontend:** Streamlit


## 🚀 Features

* **Text preprocessing (cleaning, stopword removal)
* **TF-IDF vectorization
* **Multiple ML models (Logistic Regression, Naive Bayes, SVM)
* **Best model selection based on accuracy
* **Streamlit-based interactive web app
* **Modular and scalable project structure

## 📁 Project Structure
FAKENEWSDETECTOR
│
├── data
│ ├── raw
│ │ ├── Fake.csv
│ │ └── True.csv
│ └── processed
│
├── models
│ ├── classifier.pkl
│ └── tfidf_vector.pkl
│
├── notebooks
│ └── EDA_and_Model.ipynb
│
├── src
│ ├── preprocessing.py
│ ├── predictor.py
│ └── app.py
│
├── requirements.txt
└── README.md

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the training notebook to generate models.
3. Launch the app: `streamlit run src/app.py`

## 📊 Algorithms Used

1. TF-IDF Vectorizer
2. Logistic Regression
3. Multinomial Naive Bayes
4. Support Vector Machine (SVM)

## 👩‍💻 Author

Rashmi Kumari
B.Tech (Cyber Security)