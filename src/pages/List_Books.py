import streamlit as st
from api.books import Book

st.set_page_config(page_title="List of Books",layout='wide')

st.header('List of Books')
books = Book().get_books()

if books:
    for book in books:
        st.write(f'## {book.title}')
        st.text(f'ISBN: {book.isbn}')
        st.text(f'Author: {book.author}')
        st.text(f'Description: {book.description}')
        st.text(f'Category: {book.category}')
        st.text(f'Date Acquisition: {book.date_acquisition}')
        st.text(f'Conservation Status: {book.conservation_status}')
        st.text(f'Physical Location: {book.physical_location}')
        st.text(f'Book Cover url: {book.book_cover_url}')
        st.text(f'Status: {book.status}')
        
        st.text('')
        st.text('')