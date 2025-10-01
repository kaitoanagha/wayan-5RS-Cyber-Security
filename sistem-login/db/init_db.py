# db/init_db.py
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # seed contoh user (password plain text untuk testing CodeQL)
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    except Exception:
        pass

    conn.commit()
    conn.close()
    print("DB initialized at:", DB_PATH)

if __name__ == "__main__":
    init_db()
