from decouple import config
import psycopg2
from passlib.hash import postgres_md5

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

class User:
    def __init__(
            self, 
            id = None, 
            username = None, 
            first_name = None, 
            last_name = None, 
            password = None, 
            user_photo_url = None, 
            role = None
        ):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.user_photo_url = user_photo_url
        self.role = role

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

    def authenticate_user(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()

            cur.execute('SELECT * FROM Users WHERE username = %s', (self.username,))
            user = cur.fetchone()

            if user:
                user_id, stored_username, hashed_password, first_name, last_name, user_photo_url, role = user

                hashed_input_password = postgres_md5.hash(self.password)

                if postgres_md5.verify(self.password, hashed_password):
                    print(f'User with ID {user_id} authenticated successfully.')
                    conn.close()
                    return User(
                        user_id,
                        stored_username,
                        first_name,
                        last_name,
                        user_photo_url,
                        role
                    )
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

    def create_user(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Users (username, first_name, last_name, password, user_photo_url, role) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    self.username,
                    self.first_name,
                    self.last_name,
                    self.password,
                    self.user_photo_url,
                    self.role
                )
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error inserting user: {e}')
            return False

    def update_user(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Users SET username = %s, first_name = %s, last_name = %s, password = %s, user_photo_url = %s, role = %s WHERE id = %s",
                (
                    self.username,
                    self.first_name,
                    self.last_name,
                    self.password,
                    self.user_photo_url,
                    self.role,
                    self.id
                )
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error updating user: {e}')
            return False

    def delete_user(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Users WHERE id = %s",
                (self.id,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error deleting user: {e}')
            return False

    def get_users(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Users')
            users_data = cur.fetchall()
            conn.close()

            users = []
            for user_data in users_data:
                user = User(*user_data)
                users.append(user)

            return users
        except Exception as e:
            print(f'Error fetching users: {e}')

    def get_user_by_id(self):
        try:
            conn = self.bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Users WHERE id = %s', (self.id,))
            user_data = cur.fetchone()
            conn.close()

            if user_data:
                user = User(*user_data)
                return user
        except Exception as e:
            print(f'Error fetching user: {e}')

    def get_all_members(self):
        try:
            conn = self.bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Users WHERE role = MEMBER')
            user_data = cur.fetchone()
            conn.close()
            if user_data:
                user = User(*user_data)
                return user
        except Exception as e:
            print(f'Error fetching user: {e}')