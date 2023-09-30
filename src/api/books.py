from decouple import config
import psycopg2

# Lê as variáveis de ambiente do arquivo .env
POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

# Conecte-se ao banco de dados

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

# Funções para interagir com o banco de dados (inserir, listar, etc.)

def create(title, author, publication_year):
    try:
        conn = bd_connect()

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO books (title, author, publication_year) VALUES (%s, %s, %s)",
            (title, author, publication_year)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f'Error inserting book: {e}')
        return False
    finally:
        if conn:
            conn.close()

# Função para listar os livros no banco de dados
def get():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM books')
        books = cur.fetchall()
        return books
    except Exception as e:
        print(f'Error fetching books: {e}')
    finally:
        if conn:
            conn.close()