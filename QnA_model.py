from transformers import pipeline
import sent_preprocessing as sp
import pandas as pd

pdf_df = pd.DataFrame(sp.sentences, columns=['text'])
text = "".join(pdf_df)

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def ask_question(query):
    prompt = f"question: {query}  context: {text}"
    # result = qa(prompt, max_new_tokens=1024)
    result = qa({"question": query, "context": text})
    answer = result["answer"]
    return answer
