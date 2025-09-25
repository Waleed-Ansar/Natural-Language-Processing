from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
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
    df = pd.DataFrame(context, columns=['text'])
    pd.set_option("display.max_colwidth", 100)
    lines = df
    # input_text = f"question: {question}  context: keeping the book in consideration {lines}"
    input_text = f"""
    You are a helpful book assistant.
    Answer the question only using the context provided.

    question: {question}
    context: {lines}
    """
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    out = model.generate(**inputs, max_length=max_length, num_beams=4)
    return tokenizer.decode(out[0], skip_special_tokens=True)


# python sent_preprocessing.py



















