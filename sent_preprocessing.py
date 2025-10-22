from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from nltk.tokenize import sent_tokenize
from transformers import pipeline
import pandas as pd
import nltk
import re
import os

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# ==== Importing and Reading Data ====

context = []
sentences = []
book = []
tokens = []

def s_main(pdf, pdf_fitz):
    global book
    book = pdf

    global context
    context = pdf_fitz
    
    global text
    text = book
    text = re.sub(r'\\n', "", text)

    global tokens
    tokens = sent_tokenize(text)

    global sentences
    for token in tokens:
        sentences.append(token)


tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")

def ask_question(question: str, max_length=64):
    key = os.getenv('api_key')
    client = OpenAI(api_key=key)

    prompt = f"""
        Answer the question: '{question}'  based on the provided context only containing data
        from context\n{file}\n\n if exists in the context otherwise tell nothing is present in context
        related to your question.
    """

    resp = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {"role": "system", "content": "You are a helpful assistant who is master in answering questions based on given context in only one line and strictly related to topic."},
            {"role": "user", "content": f"{prompt}"}
        ],
        temperature=0.5
    )

    response = resp.choices[0].message.content
    return response


# python sent_preprocessing.py




















