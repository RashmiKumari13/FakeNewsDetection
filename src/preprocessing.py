import re
import pandas as pd

def clean_text_fast(x):
    """
    Clean a single news text input.
    Works with strings, lists, numbers, NaN, or dicts.
    """
    # Handle NaN
    if pd.isna(x):
        text = ""
    # If input is a list, join into a single string
    elif isinstance(x, list):
        text = " ".join([str(i) for i in x])
    # If input is a dict with 'text', extract it
    elif isinstance(x, dict) and 'text' in x:
        text = str(x['text'])
    else:
        # If it's a string or number, just convert to str
        text = str(x)

    # Clean the text
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = text.strip()

    return text
