from wordcloud import WordCloud
from word_preprocessing import w_main
import word_preprocessing as wp
from sent_preprocessing import s_main
import sent_preprocessing as sp
from PyPDF2 import PdfReader
import QnA_model as qa
import importlib
import streamlit as st
import pandas as pd
import trns


st.title("Natural Language Processing Statistics")
st.subheader("Upload PDF to Check Statistics")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

st.text('"NOTE: Dummy data is already available for checking, you can continue or upload your own pdf."')
st.warning("Make sure to 'reset' before uploading to prevent data mixing!")

row = st.columns(5)

text = ""
with row[0]:
    if st.button("upload"):
        if uploaded_file is None:
            st.error("Upload file first!")
        else:
            pdf_reader = PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"

with row[1]:
    if st.button("continue"):
        path = "the-strange-case-of-doctor-jekyll-and-mr-hyde-robert-louis-stevenson.pdf"
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

if text:
    pdf_file = text
    w_main(pdf_file)
    s_main(pdf_file)
else:
    pdf_file = ""
    w_main(pdf_file)
    s_main(pdf_file)

s_df = pd.DataFrame(sp.sentences, columns=['text'])
s_df = s_df[s_df["text"] != "."]

text = " ".join(wp.clean_words)
if text is not "":
    word_cloud = WordCloud(background_color="white", max_words=1000).generate(text)
else:
    st.error("UPLOAD FILE FIRST OR PRESS 'CONTINUE' TO CHECK WITH DUMMY DATA.")

counts = wp.counts
pos = wp.pos
ner = wp.ner_words

st.subheader("Show Word Cloud:")
if st.button("Show image"):
    if text is not "":
        st.image(word_cloud.to_array(), use_container_width=True)
    else:
        st.error("UPLOAD FILE FIRST OR PRESS 'CONTINUE' TO CHECK WITH DUMMY DATA.")

st.subheader("Show All Lines:")
if st.button("Show sentences"):
    st.dataframe(s_df)

st.subheader("Show Word Frequency Count:")
if st.button("Show words"):
    st.dataframe(counts)

st.subheader("Enter Word to Check Frequency:")
word = st.text_input("Enter:")
if st.button("Enter word"):
    if word:
        st.text(wp.search_word(word.lower()))

st.subheader("Show All words POS:")
if st.button("Show pos"):
    st.dataframe(pos)

st.subheader("Enter Word to Check POS:")
wrd = st.text_input("Enter word for POS:")
if st.button("Search POS"):
    if wrd:
        st.dataframe(wp.search_pos(wrd.lower()))

st.subheader("Ask a Question about Article:")
query = st.text_input("Question")
if st.button("Ask"):
    if query:
        st.text(trns.ask_question(query.lower()))
st.subheader("Show NER:")
if st.button("show ner"):
    st.dataframe(wp.all_ners())

st.subheader("Enter Word to Check NER:")
wrd = st.text_input("Enter")
if st.button("click"):
    st.dataframe(wp.search_ner(wrd.capitalize()))

st.subheader("Ask a Question about Article:")
query = st.text_input("Question")
if st.button("ask"):
    st.text(qa.ask_question(query))

with row[3]:
    if st.button("reset"):
        importlib.reload(wp)
        importlib.reload(sp)
        importlib.reload(qa)
        st.session_state.clear()


# streamlit run main.py























