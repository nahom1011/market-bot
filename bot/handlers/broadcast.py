from telegram import Update
from telegram.ext import ContextTypes
from database import users
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def broadcast_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Only admin allowed (simplify here)
    admin_id = int(os.getenv("ADMIN_ID", 0))
    if update.effective_user.id != admin_id:
        await update.message.reply_text("You are not authorized to use this.")
        return

    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("Usage: /broadcast <message>")
        return

    user_ids = users.get_all_user_ids()
    success = 0
    failed = 0

    for user_id in user_ids:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
            success += 1
        except:
            failed += 1

    await update.message.reply_text(f"Broadcast done.\nSuccess: {success}\nFailed: {failed}")
