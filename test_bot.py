import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

load_dotenv()
BOT_TOKEN = "8030579167:AAF0gTeNvsx6u9ZqCguFcvtuhwLppj6aeOM"
print("BOT TOKEN:", BOT_TOKEN)

async def start(update, context):
    await update.message.reply_text("Bot is alive!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
