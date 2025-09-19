from transformers import pipeline
import sent_preprocessing as sp
import pandas as pd


pdf_df = pd.DataFrame(sp.sentences, columns=['text'])
text = "".join(pdf_df)

qa = pipeline("text2text-generation", model="google/flan-t5-small")

def ask_question(query):
    prompt = f"question: {query}  context: {text}"
    result = qa(prompt, max_new_tokens=1024)
    return (f"{result[0]['generated_text']}\n")







