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

def create_book(book):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Books (isbn, title, author, description, category, date_acquisition, conservation_status, physical_location, book_cover_url, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                book["isbn"], 
                book["title"], 
                book["author"], 
                book["description"],
                book["category"], 
                book["date_acquisition"], 
                book["conservation_status"], 
                book["physical_location"], 
                book["book_cover_url"], 
                book["status"], 
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error inserting book: {e}')
        return False
    

def update_book(book):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "UPDATE Books SET title = %s, author = %s, description = %s, category = %s, date_acquisition = %s, conservation_status = %s, physical_location = %s, book_cover_url = %s, status = %s WHERE isbn = %s",
            (
                book['title'], 
                book['author'], 
                book['description'],
                book['category'], 
                book['date_acquisition'], 
                book['conservation_status'], 
                book['physical_location'], 
                book['book_cover_url'], 
                book['status'], 
                book['isbn'])
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error updating book: {e}')
        return False

def delete_book(isbn):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM Books WHERE isbn = %s",
            (isbn)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error deleting book: {e}')
        return False

def get_book():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Books')
        books = cur.fetchall()
        conn.close()
        return books
    except Exception as e:
        print(f'Error fetching books: {e}')

def get_book_by_isbn(isbn):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Books WHERE isbn = %s', (isbn))
        books = cur.fetchall()
        conn.close()
        return books
    except Exception as e:
        print(f'Error fetching books: {e}')

def get_available_books():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Books WHERE status = 'AVAILABLE'")
        available_books = cur.fetchall()
        conn.close()
        return available_books
    except Exception as e:
        print(f'Error fetching available books: {e}')