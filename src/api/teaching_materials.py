from db import Database

# TODO: Atualizar as funções exemplo para funcionarem com o banco correto
def create():
    try:
        conn = Database()

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Teaching_Materials"
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
        cur.execute('SELECT * FROM Teaching_Materials')
        teaching_materials = cur.fetchall()
        return teaching_materials
    except Exception as e:
        print(f'Error fetching teaching_materials: {e}')
    finally:
        if conn:
            conn.close()