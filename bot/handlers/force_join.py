from telegram import Update
from telegram.ext import ContextTypes
import os

CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Simple text reminder (replace with real Telegram API check for member status if you want)
    await update.message.reply_text(f"Please join our channel {CHANNEL_USERNAME} to continue.")
