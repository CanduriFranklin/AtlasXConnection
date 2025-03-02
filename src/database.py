# src/database.py
import psycopg2
from .config import DB_CONFIG

def get_connection():
    """
    Establece una conexión con la base de datos PostgreSQL.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def execute_query(query, params=None):
    """
    Ejecuta una consulta en la base de datos.
    """
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                if query.strip().upper().startswith("SELECT"):
                    result = cursor.fetchall()
                else:
                    conn.commit()
                    result = None
            return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        finally:
            conn.close()
    return None