from transformers import pipeline
import sent_preprocessing as sp

text = "".join(sp.book[25:475])

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")


def ask_question(query):
  context = text
  question = query
  
  result = qa(question=question, context=context, batch_size=2, top_k=2, max_answer_len=30)
  answer = result["answer"]
  return answer


