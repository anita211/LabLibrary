from decouple import config
import psycopg2

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

def bd_connect():
    try:
        conn = psycopg2.connect(
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host="localhost",
            port=POSTGRES_PORT
        )
        return conn
    except Exception as e:
        print(f'Error connecting to the database: {e}')

def create_loan(loan_data):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Loan (loan_date, expected_return_date, status, id_book, id_material, id_user) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                loan_data["loan_date"],
                loan_data["expected_return_date"],
                loan_data.get("status", "IN_PROGRESS"),
                loan_data.get("id_book"),
                loan_data.get("id_material"),
                loan_data["id_user"]
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error creating loan: {e}')
        return False

def update_loan_status(loan_id, new_status):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "UPDATE Loan SET status = %s WHERE id = %s",
            (new_status, loan_id)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error updating loan status: {e}')
        return False

def delete_loan(loan_id):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM Loan WHERE id = %s",
            (loan_id,)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error deleting loan: {e}')
        return False

def get_all_loans():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Loan')
        loans = cur.fetchall()
        conn.close()
        return loans
    except Exception as e:
        print(f'Error fetching loans: {e}')
        return None
    
def get_in_progress_loans():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Loan WHERE status = 'IN_PROGRESS'")
        in_progress_loans = cur.fetchall()
        conn.close()
        return in_progress_loans
    except Exception as e:
        print(f'Error fetching in-progress loans: {e}')
        return None