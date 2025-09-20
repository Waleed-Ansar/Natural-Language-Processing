from nltk.tokenize import sent_tokenize
import pandas as pd
import nltk
import fitz
import re

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# ==== Importing and Reading Data ====

sentences = []
book = []

def s_main(pdf):
    global book
    book = pdf

    global text
    text = book
    text = re.sub(r'\\n', "", text)

    tokens = sent_tokenize(text)

    global sentences
    for token in tokens:
        sentences.append(token)


# python sent_preprocessing.py




