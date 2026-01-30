from flask import Flask, request, render_template_string
from src.predictor import predict_news
import streamlit as st
from predictor import predict_news

app = Flask(__name__)

HTML = """
<h2>📰 Fake News Detection</h2>
<form method="post">
<textarea name="news" rows="10" cols="60"></textarea><br><br>
<input type="submit" value="Check News">
</form>
<h3>{{ result }}</h3>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        news = request.form["news"]
        result = predict_news(news)
    return render_template_string(HTML, result=result)


st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detection App")
st.write("Enter a news article below and check whether it is **REAL or FAKE**.")

news_text = st.text_area("Paste News Content Here", height=250)

if st.button("Check News"):
    if news_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        result = predict_news(news_text)
        if "REAL" in result:
            st.success(result)
        else:
            st.error(result)

if __name__ == "__main__":
    app.run(debug=True)
