from db import Database

# TODO: Atualizar as funções exemplo para funcionarem com o banco correto
def create():
    try:
        conn = Database()

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Loan"
        )
        conn.commit()
        return True
    except Exception as e:
        print(f'Error: {e}')
        return False
    finally:
        if conn:
            conn.close()

def get():
    try:
        conn = Database()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Loan')
        loan = cur.fetchall()
        return loan
    except Exception as e:
        print(f'Error fetching loan: {e}')
    finally:
        if conn:
            conn.close()