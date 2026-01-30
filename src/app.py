import streamlit as st
import sys
import os

# Ensure the 'src' directory is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from predictor import predict_news

st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detection App")
st.write("Enter a news article below to check its authenticity.")

news_text = st.text_area("Paste News Content Here", height=250)

if st.button("Check News"):
    if news_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        with st.spinner('Analyzing...'):
            result = predict_news(news_text)
            if "REAL" in result:
                st.success(result)
            else:
                st.error(result)