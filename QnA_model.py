from transformers import pipeline
import sent_preprocessing as sp

text = "".join(sp.book[4:106])

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def ask_question(query):
    result = qa({"question": query, "context": text})
    answer = result["answer"]
    return answer

