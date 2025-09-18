from nltk.tokenize import word_tokenize
from spacy.lang.en.stop_words import STOP_WORDS
from flair.models import SequenceTagger
from nltk import WordNetLemmatizer
from flair.data import Sentence
from nltk import FreqDist
import pandas as pd
from spacy.cli import download
import subprocess
import unicodedata
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

def search_pos(word):
    words = list(set(clean_words))
    if word in words:
        pos_list = []
        pos_list.append(word)
        query_pos = nltk.pos_tag(pos_list)
        return query_pos

# ==== NER ====
def all_ners():
    ners = []
    
    words = list(set(clean_words))
    words = words[3000:4000]
    tagger = SequenceTagger.load("ner")
    for word in words:
        sentence = Sentence(word)
        tagger.predict(sentence)
        formatted = [f'"{entity.text}" --> {entity.get_label("ner").value}' for entity in sentence.get_spans('ner')]
        if formatted != []:
            ners.append(formatted)
    return ners

def search_ner(word):
    sentence = Sentence(word)
    tagger.predict(sentence)
    formatted = [f'"{entity.text}" --> {entity.get_label("ner").value}' for entity in sentence.get_spans('ner')]
    return formatted

# ==== Counting Data ====
counts = FreqDist(clean_words)

def search_word(word):
    query_count = FreqDist(clean_words)
    count = query_count[word]
    return count



# python word_preprocessing.py

























