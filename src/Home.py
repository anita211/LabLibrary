import streamlit as st

with open('src/globals.py', 'r') as file:
    exec(file.read())

st.title('Book Manager')

st.text('')

if st.button("Logout", use_container_width=True):
    with open('src/globals.py', 'w') as file:
        file.write(f"logged_user = {None}")

