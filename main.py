from wordcloud import WordCloud
import matplotlib.pyplot as plt
import word_preprocessing as wp
import sent_preprocessing as sp
import streamlit as st
import pandas as pd
import numpy as np

wp.download()
s_df = pd.DataFrame(sp.sentences, columns=['text'])
s_df = s_df[s_df["text"] != "."]

text = " ".join(wp.clean_words)

word_cloud = WordCloud(background_color='white', max_words=1000).generate(text)

# c_df = pd.DataFrame(wp.counts)


st.title("Natural Language Processing Statistics")

st.subheader("Show Word Cloud:")
if st.button('show image'):
    st.image(word_cloud.to_array(), use_container_width=True)

st.subheader("Show All Lines Separately")
if st.button('show sentences'):
    st.table(s_df)

st.subheader("Show Word Frequency Count:")
if st.button('show words'):
    st.table(wp.counts)

st.subheader("Enter Word to Check Frequency:")
word = st.text_input("Enter:" )
if st.button('enter'):
    st.text(wp.search_word(word.lower()))

st.subheader("Show All words POS:")
if st.button('show pos'):
    st.table(wp.pos)

# st.subheader("Show NER:")
# if st.button('show ner'):
#     st.table(wp.ner_words)


# streamlit run main.py

