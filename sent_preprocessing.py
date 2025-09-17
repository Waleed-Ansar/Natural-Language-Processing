from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import unicodedata
import string
import spacy
import nltk
import fitz
import re

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# ==== Importing and Reading Data ====
doc = fitz.open("John M. Barry - The Great Influenza - The story of the deadliest pandemic in history.pdf")
length = len(doc)

book = []
for i in range(length):
    page = doc[i]
    text = page.get_text()
    book.append(text)

df = pd.DataFrame(book)
# df.to_csv('pdf_to_csv.csv', index=False)

text = " ".join(book)

text = re.sub(r'\\n', "", text)

sentences = sent_tokenize(text)



# python sent_preprocessing.py
