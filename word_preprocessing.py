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
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="average")

# ==== Importing and Reading Data ====
clean_words = []
ner_words = []

def w_main(pdf):
    global book
    book = pdf

    global text
    text = book

    global tokens
    tokens = word_tokenize(text)

    global words
    words = " ".join(tokens)
    
    # ==== Cleaning Data ====
    words = unicodedata.normalize("NFKC", words)
    words = re.findall(r"[A-Za-zÀ-ÿ]+", words)

    global clean_words
    clean_words = []
    
    # ==== Lemmatizitation ====
    lemmatizer = WordNetLemmatizer()
    
    for word in words:
        if word not in STOP_WORDS and not len(word) <= 3:
            word = lemmatizer.lemmatize(word)
            word = re.sub(r'\\n', "", word)
            clean_words.append(word.lower())
    
    # ==== POS ====
    global pos
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
    
result = []
def all_ners():
    entities = ner(text)

    global results
    
    for entity in entities:
        entity_type = entity.get('entity_group', entity.get('entity', 'UNKNOWN'))
        entity_name = entity['word']
        result.append(f"{entity_name} --> {entity_type}")
     
        return (set(result))
ners = []
def search_ner(word):
global ners

results = ner(word)
for entity in results:
    entity_type = entity.get('entity_group', entity.get('entity', 'UNKNOWN'))
    entity_name = entity['word']
    ners.append(f"{entity_name} --> {entity_type}")
return ners

# ==== Counting Data ====
global counts
counts = FreqDist(clean_words)

def search_word(word):
    query_count = FreqDist(clean_words)
    count = query_count[word]
    return count



# python word_preprocessing.py











































