import sqlite3
import threading

DB_LOCK = threading.Lock()

def get_connection():
    conn = sqlite3.connect("bot_data.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with DB_LOCK:
        conn = get_connection()
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            referred_by INTEGER,
            language TEXT DEFAULT 'en'
        )
        """)

        # Products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id TEXT PRIMARY KEY,
            gender TEXT,
            category TEXT,
            name_en TEXT,
            name_am TEXT,
            name_om TEXT,
            name_ti TEXT,
            image_url TEXT
        )
        """)

        # Referrals table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_id INTEGER,
            referred_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Ratings table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_id TEXT,
            rating INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()
