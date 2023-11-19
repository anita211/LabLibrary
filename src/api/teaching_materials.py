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

def create_teaching_material(material):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Teaching_materials (description, category, date_acquisition, serie_number, conservation_status, physical_location, material_cover_url, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                material["description"], 
                material["category"], 
                material["date_acquisition"], 
                material["serie_number"],
                material["conservation_status"], 
                material["physical_location"], 
                material["material_cover_url"], 
                material["status"]
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error inserting teaching material: {e}')
        return False

def update_teaching_material(material):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "UPDATE Teaching_materials SET description = %s, category = %s, date_acquisition = %s, serie_number = %s, conservation_status = %s, physical_location = %s, material_cover_url = %s, status = %s WHERE id = %s",
            (
                material['description'], 
                material['category'], 
                material['date_acquisition'], 
                material['serie_number'], 
                material['conservation_status'], 
                material['physical_location'], 
                material['material_cover_url'], 
                material['status'], 
                material['id']
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error updating teaching material: {e}')
        return False

def delete_teaching_material(material_id):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM Teaching_materials WHERE id = %s",
            (material_id,)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'Error deleting teaching material: {e}')
        return False

def get_teaching_materials():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Teaching_materials')
        materials = cur.fetchall()
        conn.close()
        return materials
    except Exception as e:
        print(f'Error fetching teaching materials: {e}')

def get_teaching_material_by_id(material_id):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Teaching_materials WHERE id = %s', (material_id))
        material = cur.fetchone()
        conn.close()
        return material
    except Exception as e:
        print(f'Error fetching teaching material: {e}')

def get_teaching_material_by_serie_number(serie_number):
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Teaching_materials WHERE serie_number = %s', (serie_number))
        material = cur.fetchone()
        conn.close()
        return material
    except Exception as e:
        print(f'Error fetching teaching material: {e}')

def get_available_teaching_materials():
    try:
        conn = bd_connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Teaching_materials WHERE status = 'AVAILABLE'")
        available_materials = cur.fetchall()
        conn.close()
        return available_materials
    except Exception as e:
        print(f'Error fetching available teaching materials: {e}')
