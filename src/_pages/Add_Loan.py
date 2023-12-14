import streamlit as st
from api.users import User
from api.books import Book
from api.loan import Loan
from api.teaching_materials import TeachingMaterial
import datetime
from globals import logged_user

def find_item_by_id(id, list):
    for item in list:
        if item.id == id:
            return item
        
def find_item_by_isbn(isbn, list):
    for item in list:
        if item.isbn == isbn:
            return item

def get_name(user):
    return user.first_name + ' ' + user.last_name

def create_page():

    st.header('Add a New Loan')
    LoanTypes = ['BOOK', 'TEACHING_MATERIAL']
    Books = Book().get_available_books()
    Books = [book for book in Books if book.status == 'AVAILABLE']
    BooksId = [book.isbn for book in Books]
    TeachingMaterials = TeachingMaterial().get_available_teaching_materials()
    TeachingMaterials = [tm for tm in TeachingMaterials if tm.status == 'AVAILABLE']
    TeachingMaterialsId = [tm.id for tm in TeachingMaterials]
    ObjectType = st.selectbox('Object Type', LoanTypes)

    if logged_user["role"] == "ADMIN":
        users_list = User().get_users()

    # Diferencia os campos de Livro e Material Didático
    if ObjectType == 'BOOK':

        st.write('Book')
        book_id = st.selectbox('Book ISBN', BooksId, format_func=lambda x: find_item_by_isbn(x, Books).title)
        if BooksId != []:
            st.write("Book Name - " + Book(book_id).get_book_by_isbn().title)
    else:
        st.write('Teaching Material')
        teaching_material_id = st.selectbox('Teaching Material ID', TeachingMaterialsId, format_func=lambda x: find_item_by_id(x, TeachingMaterials).description)
        if TeachingMaterialsId != []:
            st.write('Serial Number - ' + TeachingMaterial(teaching_material_id).get_teaching_material_by_id().serie_number)

    # Diferencia os campos dependedo do tipo de usuário
    loan_date = st.date_input('Loan Date')

    if logged_user["role"] == "MEMBER":
        loan_status='IN_PROGRESS'
        id_user = logged_user["id"]
        expected_return_date = datetime.date.today() + datetime.timedelta(days=7) # default - 7 dias a partir da data atual

    elif logged_user["role"] == "ADMIN":

        id_user = st.selectbox('User', [user.id for user in users_list], format_func=lambda x: get_name(find_item_by_id(x, users_list)))
        st.write('Name - ' + User(id_user).get_user_by_id().first_name)
        default_date = datetime.date.today() + datetime.timedelta(days=7)
        expected_return_date = st.date_input('Expected Return Date', default_date)
        loan_status='IN_PROGRESS'


    if st.button('Confirm'):
        new_loan = Loan(
            loan_date=loan_date,
            expected_return_date=expected_return_date,
            status=loan_status,
            id_book=book_id if ObjectType == 'BOOK' else None,
            id_material=teaching_material_id if ObjectType == 'TEACHING_MATERIAL' else None,
            id_user=id_user,
        )
        
        if new_loan.create_loan():
            st.success('Loan inserted successfully!')
        else:
            st.error('Error inserting loan.')
