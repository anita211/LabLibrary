# ListBooks.py
import streamlit as st
from api.books import Book

# Define a function to generate a unique color for each book
def get_book_color(book_index):
    colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
    return colors[book_index % len(colors)]

st.set_page_config(page_title="List of Books", layout='wide')

st.header('List of Books')
books = Book().get_books()

if books:
    for index, book in enumerate(books):
        # Generate a unique color for each book
        background_color = get_book_color(index)

        # Apply custom styling with a colored background
        st.markdown(
            f'<div style="display: flex; align-items: center; justify-content: space-between; padding: 10px; border-radius: 5px; background-color: {background_color}; color: black">'
                f'<div style="display: flex; flex-direction: column; max-width: 60%">'
                    f'<h2 style="color: black ">{book.title}</h2>'
                    f'<div style="display: flex; flex-direction: column; flex-wrap: wrap; margin-left: 20px;">'
                        f'<p>ISBN: {book.isbn}</p>'
                        f'<p>Author: {book.author}</p>'
                        f'<p>Description: {book.description}</p>'
                        f'<p>Category: {book.category}</p>'
                        f'<p>Date Acquisition: {book.date_acquisition}</p>'
                        f'<p>Conservation Status: {book.conservation_status}</p>'
                        f'<p>Physical Location: {book.physical_location}</p>'
                        f'<p>Status: {book.status}</p>'
                    f'</div>'
                f'</div>'
                f'<img src="{book.book_cover_url}" alt="Book Cover" style="height: 40%; max-width: 35%; margin-right: 20px;">'
            f'</div>',
            unsafe_allow_html=True
        )

        st.text('')
