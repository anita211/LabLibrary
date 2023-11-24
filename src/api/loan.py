from decouple import config
import psycopg2

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

class Loan:
    def __init__(
            self, 
            id = None, 
            loan_date = None, 
            expected_return_date = None, 
            status = None, 
            id_book = None, 
            id_material = None, 
            id_user = None,
        ):
        self.id = id
        self.loan_date = loan_date
        self.expected_return_date = expected_return_date
        self.status = status
        self.id_book = id_book
        self.id_material = id_material
        self.id_user = id_user

    def _bd_connect(self):
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

    def create_loan(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Loan (loan_date, expected_return_date, status, id_book, id_material, id_user) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    self.loan_date,
                    self.expected_return_date,
                    self.status,
                    self.id_book,
                    self.id_material,
                    self.id_user,
                )
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error creating loan: {e}')
            return False

    def update_loan_status(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Loan SET status = %s WHERE id = %s",
                (self.status, self.id)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error updating loan status: {e}')
            return False

    def delete_loan(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Loan WHERE id = %s",
                (self.id,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error deleting loan: {e}')
            return False

    def get_all_loans(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Loan')
            loans_data = cur.fetchall()
            conn.close()

            loans = []
            for loan_data in loans_data:
                loan = Loan(*loan_data)
                loans.append(loan)

            return loans
        except Exception as e:
            print(f'Error fetching loans: {e}')
            return None
        
    def get_loans_by_id(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Loan WHERE id = %s', (self.id,))
            loans_data = cur.fetchone()
            conn.close()

            if loans_data:
                loan = Loan(*loans_data)
                return loan

        except Exception as e:
            print(f'Error fetching loans: {e}')
        
    def get_in_progress_loans(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Loan WHERE status = 'IN_PROGRESS'")
            in_progress_loans = cur.fetchall()
            conn.close()

            loans = []
            for loan_data in in_progress_loans:
                loan = Loan(*loan_data)
                loans.append(loan)

            return loans
        except Exception as e:
            print(f'Error fetching in-progress loans: {e}')
            return None