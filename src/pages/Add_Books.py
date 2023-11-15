import streamlit as st
from api.books import create as books_create

st.header('Add a New Book')

isbn = st.text_input('isbn')
title = st.text_input('Title')
author = st.text_input('Author')
description = st.text_input('description')
category = st.selectbox("category", ['ROMANCE', 'COMEDY', 'DRAMA', 'SCIFI', 'HORROR'])
date_acquisition = st.number_input('Date Acquisition', min_value=0)
conservation_status = st.selectbox('Conservation Status', ['NEW', 'AVERAGE', 'OLD', 'DAMAGED'])
physical_location = st.text_input('Physical Location')
book_cover_url = st.text_input('Book Cover url')
status = st.selectbox("Status", ['AVAILABLE', 'BORROWED'])

if st.button('Save'):
    if books_create(
        int(isbn), 
        title, 
        author, 
        description, 
        category, 
        date_acquisition, 
        conservation_status,
        physical_location,
        book_cover_url,
        status,
    ):
        st.success('Book inserted successfully!')
    else:
        st.error('Error inserting book.')
