from nltk.tokenize import word_tokenize
from spacy.lang.en.stop_words import STOP_WORDS
from nltk import WordNetLemmatizer
from nltk import FreqDist
import pandas as pd
import subprocess
import unicodedata
import spacy
import nltk
import fitz
import re

pip install 'en_core_web_sm'
# subprocess.run(["python -m spacy download en_core_web_sm"])
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

tokens = word_tokenize(text)

words = " ".join(tokens)

# ==== Cleaning Data ====
words = unicodedata.normalize("NFKC", words)
words = re.findall(r"[A-Za-zÀ-ÿ]+", words)

clean_words = []

# ==== Lemmatizitation ====
lemmatizer = WordNetLemmatizer()

for word in words:
    if word not in STOP_WORDS and not len(word) <= 3:
        word = lemmatizer.lemmatize(word)
        word = re.sub(r'\\n', "", word)
        clean_words.append(word.lower())

# ==== POS ====
pos = nltk.pos_tag(list(set(clean_words)))

# ==== NER ====
txt = " ".join(list(set(clean_words)))
ner = spacy.load('en_core_web_sm')
ner_tokens = ner(txt)

ner_words = []
for token in ner_tokens.ents:
    ner_words.append(f"{token}, {token.label_}")

# ==== Counting Data ====
counts = FreqDist(clean_words)

def search_word(word):
    query_count = FreqDist(clean_words)
    count = query_count[word]
    return count



# python word_preprocessing.py









