import streamlit as st
import requests
import re
from fastapi import APIRouter, FastAPI
from api import API
import threading
import uvicorn

app = FastAPI()
router = APIRouter()
api = API()

router.include_router(api.router)

app.include_router(router, prefix='/book_ai')


def run_api():
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

threading.Thread(target=run_api, daemon=True).start()

API_URL = "http://localhost:8000/book_ai"

st.markdown("<h1 style='color: cyan;'>AI Book Generator</h1>", unsafe_allow_html=True)

try:
    response = requests.get(f"{API_URL}/get_all_books")

    st.markdown("<h2 style='color: yellow;'>Generate a Book:</h2>", unsafe_allow_html=True)
    input = st.text_input('Describe the type of book to generate')

    param = {
        "topic": input
    }

    if st.button('Generate'):
        response = requests.post(f"{API_URL}/create_book", params=param)
        if response.status_code == 200:
            st.cache_data.clear()
            st.success('Your book is generated.')
    
    names = []
    response = requests.get(f"{API_URL}/get_all_books")
    if response.status_code == 200:
        books = response.json()
        docs = books['data']

        for i, doc in enumerate(docs):
            id = docs[i]
            ttl = id['Title']
            ttl = re.sub(r'[\*"]', "", ttl)
            names.append(ttl)

    st.markdown("<h2 style='color: yellow;'>Read Book:</h2>", unsafe_allow_html=True)
    name = st.selectbox('Select a book', options=names)
    if st.button('Read'):
        response = requests.get(f"{API_URL}/get_by_name/{name}")
        if response.status_code == 200:
            books = response.json()
            book = books['data']
            st.header(name)
            st.markdown(book[0])


    with st.sidebar:
        st.markdown("<h2 style='color: red;'>Delete Book:</h2>", unsafe_allow_html=True)
        del_title = st.selectbox('Check the book to delete:', options=names)
        if st.button('Delete'):
            title = {"title": del_title}
            response = requests.delete(f"{API_URL}/delete_book", params=title)
            if response.status_code == 200:
                st.success(f'Book: "{del_title}" is deleted.')

except:

    st.error("Run API Server First!")



