import sqlite3

DB_NAME = "students.db"

def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()