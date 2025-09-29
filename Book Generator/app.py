import streamlit as st
import requests
import re


API_URL = "http://localhost:8000/book_ai"

st.title("AI Books Generator")


try:
    response = requests.get(f"{API_URL}/get_all_books")

    st.header("Generate a Book:")
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

    st.header("Read Books:")
    name = st.selectbox('Select a book', options=names)
    if st.button('search'):
        response = requests.get(f"{API_URL}/get_by_name/{name}")
        if response.status_code == 200:
            books = response.json()
            book = books['data']
            st.header(name)
            st.markdown(book[0])


    with st.sidebar:
        st.subheader("Delete book:")
        del_title = st.selectbox('Check the book to delete:', options=names)
        if st.button('delete'):
            title = {"title": del_title}
            response = requests.delete(f"{API_URL}/delete_book", params=title)
            if response.status_code == 200:
                st.success(f'Book: "{del_title}" is deleted.')

except:
    st.error("Run API Server First!")