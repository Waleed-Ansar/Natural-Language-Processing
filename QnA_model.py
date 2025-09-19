from transformers import pipeline
import sent_preprocessing as sp
import pandas as pd

# pdf_df = pd.DataFrame(sp.sentences, columns=['text'])
# text = "".join(pdf_df)

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def ask_question(query):
    result = qa({"question": query, "context": sp.text})
    answer = result["answer"]
    return answer


