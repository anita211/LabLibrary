from db import Database

# TODO: Atualizar as funções exemplo para funcionarem com o banco correto
def create():
    try:
        conn = Database()

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Books"
        )
        conn.commit()
        return True
    except Exception as e:
        print(f'Error inserting book: {e}')
        return False
    finally:
        if conn:
            conn.close()

def get():
    try:
        conn = Database()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Books')
        books = cur.fetchall()
        return books
    except Exception as e:
        print(f'Error fetching books: {e}')
    finally:
        if conn:
            conn.close()