from nltk.tokenize import sent_tokenize
from transformers import pipeline
import pandas as pd
import nltk
import re

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# ==== Importing and Reading Data ====

sentences = []
book = []
tokens = []

def s_main(pdf):
    global book
    book = pdf

    global text
    text = book
    text = re.sub(r'\\n', "", text)

    global tokens
    tokens = sent_tokenize(text)

    global sentences
    for token in tokens:
        sentences.append(token)


def ask_question(query):
    df = pd.DataFrame(book, columns=['text'])
    result = qa({"question": query, "context": df.text})
    answer = result["answer"]
    return answer


# python sent_preprocessing.py









