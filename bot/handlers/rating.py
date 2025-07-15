import json
from database.ratings import add_rating, get_average_rating

async def rating(update, context):
    try:
        data = json.loads(update.message.text)
        user_id = data['user_id']
        product_id = data['product_id']
        rating = int(data['rating'])
    except Exception:
        await update.message.reply_text("Invalid rating data.")
        return

    if rating < 1 or rating > 5:
        await update.message.reply_text("Rating must be 1 to 5.")
        return

    add_rating(user_id, product_id, rating)
    avg = get_average_rating(product_id)
    await update.message.reply_text(f"Thanks for rating! Average rating: {avg:.2f}")
