from .db import get_connection, DB_LOCK

def add_referral(referrer_id, referred_id):
    with DB_LOCK:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO referrals (referrer_id, referred_id)
            VALUES (?, ?)
        """, (referrer_id, referred_id))
        conn.commit()
        conn.close()
