from transformers import pipeline
import sent_preprocessing as sp

text = "".join(sp.book[25:475])

# Load a small QA model (lightweight for speed/memory)
qa = pipeline("question-answering", model="deepset/minilm-uncased-squad2")

# Provide context and question
context = text
# print(context)
question = "what is influenza?"

# Run QA
result = qa(question=question, context=context)

print(result["answer"])
