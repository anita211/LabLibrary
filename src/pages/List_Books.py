import streamlit as st
from api.books import Book

# Define a function to generate a unique color for each book
def get_book_color(book_index):
    colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
    return colors[book_index % len(colors)]

st.set_page_config(page_title="List of Books", layout='wide')

st.header('List of Books')

# Get search term from user input
search_term = st.text_input("Search by Title, Author, Category, ISBN, or Date Acquisition")

books = Book().get_books()

if books:
    for index, book in enumerate(books):
        # Filter books based on search term
        if (
            not search_term
            or search_term.lower() in str(book.isbn).lower()
            or search_term.lower() in book.title.lower()
            or search_term.lower() in book.author.lower()
            or search_term.lower() in book.description.lower()
            or search_term.lower() in book.category.lower()
            or search_term.lower() in str(book.date_acquisition).lower()
            or search_term.lower() in book.conservation_status.lower()
            or search_term.lower() in book.physical_location.lower()
            or search_term.lower() in book.status.lower()
            # Add more conditions as needed
        ):
            # Generate a unique color for each book
            background_color = get_book_color(index)

            # Limit the title to 23 characters
            if len(book.title) > 23:
                display_title = f'{book.title[:23]}...'
            else:
                display_title = book.title

            st.markdown(
                f'<div style="padding: 2rem; border-radius: 2rem; background-color: {background_color}; color: black; display: flex; flex-direction: row;">'
                    f'<div style="flex: 1">'
                        f'<h2 style="color: black; word-wrap: normal; max-width: 20%">{display_title}</h2>'
                        f'<div style="display: flex; flex-direction: column; flex-wrap: wrap; margin-left: 20px; word-wrap: break-word; max-width: 20rem">'
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
                    f'<img src="{book.book_cover_url}" alt="Book Cover" style="height: 50%; width: 35%; align-self: center">'
                f'</div>',
                unsafe_allow_html=True
            )

        st.text('')