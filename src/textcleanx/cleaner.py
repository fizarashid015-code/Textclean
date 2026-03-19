
import re

stop_words = {"is","a","the","this","and","to","of","in"}

def lowercase(text):
    return text.lower()

def remove_punctuation(text):
    return re.sub(r"[^\w\s]", "", text)

def remove_numbers(text):
    return re.sub(r"\d+", "", text)

def remove_stopwords(text):
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

def clean_text(text):
    text = lowercase(text)
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = remove_stopwords(text)
    return text
