import streamlit as st
from api.books import get as books_list

st.header('List of Books')
books = books_list()
if books:
    for book in books:
        st.write(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Description: {book[3]}")
