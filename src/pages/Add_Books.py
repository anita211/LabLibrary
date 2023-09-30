import streamlit as st
from api.books import create as books_create

st.header('Add a New Book')
title = st.text_input('Title')
author = st.text_input('Author')
publication_year = st.number_input('Publication Year', min_value=0)

if st.button('Save'):
    if books_create(title, author, publication_year):
        st.success('Book inserted successfully!')
    else:
        st.error('Error inserting book.')
