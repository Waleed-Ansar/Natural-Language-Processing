from transformers import pipeline
import sent_preprocessing as sp


def ask_question(query):
  text = "".join(sp.book[25:475])
  
  qa = pipeline("question-answering", model="deepset/minilm-uncased-squad2")
  
  context = text
  question = query
  
  result = qa(question=question, context=context)
  answer = result["answer"]
  return answer
