from transformers import pipeline
import sent_preprocessing as sp
import pandas as pd


qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", tokenizer="distilbert-base-cased-distilled-squad")

def ask_question(query):
 result = qa(
        {
            "question": query,
            "context": context
        },
        handle_impossible_answer=True,
        topk=1,
        max_answer_len=500,
        doc_stride=128,
        max_seq_len=512
    )
    
    # result = qa({"question": query, "context": sp.text})
    answer = result["answer"]
    return answer


