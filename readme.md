# 📰 Fake News Detection App

A Machine Learning–based Fake News Detection system that classifies news articles as **FAKE** or **REAL** using Natural Language Processing (NLP) techniques.

---

## 🚀 Features

* Text preprocessing (cleaning, stopword removal)
* TF-IDF vectorization
* Multiple ML models (Logistic Regression, Naive Bayes, SVM)
* Best model selection based on accuracy
* Streamlit-based interactive web app
* Modular and scalable project structure

---

## 📁 Project Structure

```
FAKENEWSDETECTOR
│
├── data
│   ├── raw
│   │   ├── Fake.csv
│   │   └── True.csv
│   └── processed
│
├── models
│   ├── classifier.pkl
│   └── tfidf_vector.pkl
│
├── notebooks
│   └── EDA_and_Model.ipynb
│
├── src
│   ├── preprocessing.py
│   ├── predictor.py
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

Open the notebook:

```bash
jupyter notebook notebooks/EDA_and_Model.ipynb
```

Train the model and save the `.pkl` files into the `models/` folder.

---

## 🌐 Run Web App (Streamlit)

```bash
streamlit run src/app.py
```

---

## 📊 Algorithms Used

* TF-IDF Vectorizer
* Logistic Regression
* Multinomial Naive Bayes
* Support Vector Machine (SVM)

---

## 🎯 Use Cases

* News verification platforms
* Social media monitoring
* Educational ML projects

---

## 👩‍💻 Author

**Rashmi Kumari**
B.Tech (Cyber Security)

---

