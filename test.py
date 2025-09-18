from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error
import sent_preprocessing as sp
import re

set_verbosity_error()

text = "".join(sp.book[25:475])
text = re.sub(r'\n', "", text)

model = pipeline("summarization", model="facebook/bart-large-cnn", device=0)
llm = HuggingFacePipeline(pipeline=model)

template = PromptTemplate.from_template(f"Summarize the following {text} in a meaningful way.")

summarizer_chain = template | llm
summary = summarizer_chain

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")


def ask_question(query):
  context = summary
  question = query
  
  result = qa(question=question, context=context)
  answer = result["answer"]
  return answer




