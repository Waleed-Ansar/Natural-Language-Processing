from wordcloud import WordCloud
import matplotlib.pyplot as plt
import word_preprocessing as wp
import sent_preprocessing as sp
import streamlit as st
from spacy.cli import download
import pandas as pd
import numpy as np
import QnA_model as qa


if "s_df" not in st.session_state:
    st.session_state.s_df = pd.DataFrame(sp.sentences, columns=['text'])
    st.session_state.s_df = st.session_state.s_df[st.session_state.s_df["text"] != "."]

if "word_cloud" not in st.session_state:
    text = " ".join(wp.clean_words)
    st.session_state.word_cloud = WordCloud(background_color="white", max_words=1000).generate(text)

if "counts" not in st.session_state:
    st.session_state.counts = wp.counts

if "pos" not in st.session_state:
    st.session_state.pos = wp.pos

for key in ["show_image", "show_sentences", "show_words", "show_pos", "show_ner"]:
    if key not in st.session_state:
        st.session_state[key] = False



st.title("Natural Language Processing Statistics")

st.subheader("Show Word Cloud:")
st.button("Show image", on_click=lambda: st.session_state.update(show_image=True))
if st.session_state.show_image:
    st.image(st.session_state.word_cloud.to_array(), use_container_width=True)

st.subheader("Show All Lines:")
st.button("Show sentences", on_click=lambda: st.session_state.update(show_sentences=True))
if st.session_state.show_sentences:
    st.dataframe(st.session_state.s_df)

st.subheader("Show Word Frequency Count:")
st.button("Show words", on_click=lambda: st.session_state.update(show_words=True))
if st.session_state.show_words:
    st.dataframe(st.session_state.counts)

st.subheader("Enter Word to Check Frequency:")
word = st.text_input("Enter:", key="word_input")
if st.button("Enter"):
    if st.session_state.word_input:
        st.text(wp.search_word(st.session_state.word_input.lower()))

st.subheader("Show All words POS:")
st.button("Show pos", on_click=lambda: st.session_state.update(show_pos=True))
if st.session_state.show_pos:
    st.dataframe(st.session_state.pos)

st.subheader("Enter Word to Check POS:")
wrd = st.text_input("Enter", key='input_word')
if st.button("search"):
    if st.session_state.input_word:
        st.dataframe(wp.search_pos(st.session_state.input_word.lower()))

st.subheader("Show NER:")
st.button("Show ner", on_click=lambda: st.session_state.update(show_ner=True))
if st.session_state.show_ner:
    st.dataframe(wp.all_ners())

st.subheader("Enter Word to Check NER:")
wrd = st.text_input("Enter", key='input_a_word')
if st.button("click"):
    if st.session_state.input_a_word:
        st.dataframe(wp.search_ner(st.session_state.input_a_word.capitalize())

st.subheader("Ask a Question about Article:")
query = st.text_input("Question", key='query')
if st.button("ask"):
    if st.session_state.query:
        st.text(qa.ask_question(st.session_state.query))

# streamlit run main.py




















