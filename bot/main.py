import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start, rating, webhook_handler
from database.db import init_db

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

async def on_start(update, context):
    await start.start(update, context)

async def on_rating(update, context):
    await rating.rating(update, context)

async def on_webhook(update, context):
    await webhook_handler.webhook_handler(update, context)

def main():
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.bot_data['WEB_APP_URL'] = WEB_APP_URL

    app.add_handler(CommandHandler("start", on_start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_rating))

    app.run_polling()

if __name__ == "__main__":
    main()
