from spacy.lang.en.stop_words import STOP_WORDS
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from transformers import pipeline
from flair.data import Sentence
from nltk import FreqDist
import pandas as pd
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
doc = fitz.open("the-strange-case-of-doctor-jekyll-and-mr-hyde-robert-louis-stevenson.pdf")
length = len(doc)

book = []
for i in range(length):
    page = doc[i]
    text = page.get_text()
    book.append(text)

df = pd.DataFrame(book)

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
text = "".join(book[40:106])

ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="average")

def all_ners(text):
    entities = ner(text)

    result = []
    
    for entity in entities:
        entity_type = entity.get('entity_group', entity.get('entity', 'UNKNOWN'))
        entity_name = entity['word']
        result.append(f"{entity_name} --> {entity_type}")
 
    return (set(result))

def search_ner(word):
    results = ner(word)
    for entity in results:
        return (f"{entity['word']} -> {entity['entity_group']}")

# ==== Counting Data ====
counts = FreqDist(clean_words)

def search_word(word):
    query_count = FreqDist(clean_words)
    count = query_count[word]
    return count



# python word_preprocessing.py



































