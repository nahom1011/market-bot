import hmac
import hashlib

def check_webapp_init_data(init_data, bot_token):
    """Verify Telegram WebApp initData hash according to Telegram docs"""
    data_check_string = "\n".join(
        sorted([f"{k}={v}" for k, v in init_data.items() if k != "hash"])
    )
    secret_key = hashlib.sha256(bot_token.encode()).digest()
    hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
    return hmac_hash == init_data.get("hash")
