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

# TODO: Atualizar as funções exemplo para funcionarem com o banco correto
def create():
    try:
        conn = bd_connect()

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Teaching_Materials"
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error: {e}')
        return False

def get():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Teaching_Materials')
        teaching_materials = cur.fetchall()
        return teaching_materials
    except Exception as e:
        print(f'Error fetching teaching_materials: {e}')