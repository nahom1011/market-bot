from .db import get_connection, DB_LOCK

def add_rating(user_id, product_id, rating):
    with DB_LOCK:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ratings (user_id, product_id, rating)
            VALUES (?, ?, ?)
        """, (user_id, product_id, rating))
        conn.commit()
        conn.close()

def get_average_rating(product_id):
    with DB_LOCK:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT AVG(rating) as avg_rating FROM ratings WHERE product_id=?
        """, (product_id,))
        avg = cursor.fetchone()['avg_rating']
        conn.close()
        return avg or 0
