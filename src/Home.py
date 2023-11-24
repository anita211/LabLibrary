import streamlit as st
from api.users import User

with open('src/globals.py', 'r') as file:
    exec(file.read())

with open('src/globals.py', 'w') as file:
    file.write(f"logged_user = {None}")

User(1, 'nome123', 'Pafuncio', 'Pinto', '123456', 'ADMIN').authenticate_user()

st.title('Book Manager')

