from db import Database

# TODO: Atualizar as funções exemplo para funcionarem com o banco correto
def create():
    try:
        conn = Database()

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Users"
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
        cur.execute('SELECT * FROM Users')
        users = cur.fetchall()
        return users
    except Exception as e:
        print(f'Error fetching users: {e}')
    finally:
        if conn:
            conn.close()