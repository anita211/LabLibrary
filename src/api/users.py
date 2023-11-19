from decouple import config
import psycopg2
from passlib.hash import postgres_md5

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

def authenticate_user(username, password):
    try:
        conn = bd_connect()
        cur = conn.cursor()

        cur.execute('SELECT * FROM Users WHERE username = %s', (username,))
        user = cur.fetchone()

        if user:
            user_id, stored_username, hashed_password, first_name, last_name, user_photo_url, role = user

            hashed_input_password = postgres_md5.hash(password)

            if postgres_md5.verify(password, hashed_password):
                print(f'User with ID {user_id} authenticated successfully.')
                conn.close()
                return {
                    'id': user_id,
                    'username': stored_username,
                    'first_name': first_name,
                    'last_name': last_name,
                    'user_photo_url': user_photo_url,
                    'role': role
                }
            else:
                print('Invalid password.')
                conn.close()
                return None
        else:
            print('User not found.')
            conn.close()
            return None

    except Exception as e:
        print(f'Error authenticating user: {e}')
        return None

def create_user(user):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Users (username, first_name, last_name, password, user_photo_url, role) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                user["username"], 
                user["first_name"], 
                user["last_name"], 
                user["password"],
                user["user_photo_url"], 
                user["role"]
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error inserting user: {e}')
        return False

def update_user(user):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "UPDATE Users SET username = %s, first_name = %s, last_name = %s, password = %s, user_photo_url = %s, role = %s WHERE id = %s",
            (
                user['username'], 
                user['first_name'], 
                user['last_name'],
                user['password'], 
                user['user_photo_url'], 
                user['role'], 
                user['id']
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error updating user: {e}')
        return False

def delete_user(user_id):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM Users WHERE id = %s",
            (user_id)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error deleting user: {e}')
        return False

def get_users():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Users')
        users = cur.fetchall()
        conn.close()
        return users
    except Exception as e:
        print(f'Error fetching users: {e}')

def get_user_by_id(user_id):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Users WHERE id = %s', (user_id))
        user = cur.fetchone()
        conn.close()
        return user
    except Exception as e:
        print(f'Error fetching user: {e}')

def get_user_by_username(username):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Users WHERE username = %s', (username))
        user = cur.fetchone()
        conn.close()
        return user
    except Exception as e:
        print(f'Error fetching user: {e}')