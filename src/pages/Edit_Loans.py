import streamlit as st
from api.users import User
from api.books import Book
from api.loan import Loan
from api.teaching_materials import TeachingMaterial
from globals import logged_user

user_role = logged_user["role"]
st.header('Edit Loan')

if user_role == "ADMIN":
    
    select_loan = st.selectbox('Loan ID', [loan.id for loan in Loan().get_all_loans()])

    loan = Loan(select_loan).get_loans_by_id()
    status = ['IN_PROGRESS', 'COMPLETED']

    # Exibir informações do empréstimo
    st.subheader('Current Loan Information:')
    st.write(f'ID: {loan.id}')
    st.write(f'ID User: {loan.id_user}')

    if loan.id_book == None:
        st.write(f'ID Teaching Material: {loan.id_material }')
    else:
        st.write(f'ID Book: {loan.id_book}')

    st.write(f'Loan Date: {loan.loan_date}')
    st.write(f'Expected Return Date: {loan.expected_return_date}')

    if loan.status == 'IN_PROGRESS':
        st.write(f'Status: {loan.status} (BORROWED)')
    else:
        st.write(f'Status: {loan.status} (RETURNED)')

    # Editar informações do empréstimo
    st.subheader('Edit Loan Information:')

    expected_return_date = st.date_input('Expected Return Date', loan.expected_return_date)
    loan_status = st.selectbox('Status', status, index=status.index(loan.status) )
    
    if st.button('Save Changes'):
        # Atualizar o empréstimo com as novas informações
        loan.id,
        loan.id_user= int(loan.id_user),
        loan.id_book=int(loan.id_book) if loan.id_book != None else None,
        loan.id_material=int(lona.id_material) if loan.id_book == None else None,
        loan.loan_date = loan.loan_date,
        loan.expected_return_date = expected_return_date,
        loan.status=loan_status,

        if loan.update_return_date() and loan.update_loan_status():
            st.success('Loan successfully updated.')
        else:
            st.error('Error editing loan expected date.')
 