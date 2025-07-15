from .db import get_connection, DB_LOCK

def add_user(user_id, username=None, referred_by=None, language='en'):
    with DB_LOCK:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO users (user_id, username, referred_by, language)
            VALUES (?, ?, ?, ?)
        """, (user_id, username, referred_by, language))
        conn.commit()
        conn.close()

def get_user(user_id):
    with DB_LOCK:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user
