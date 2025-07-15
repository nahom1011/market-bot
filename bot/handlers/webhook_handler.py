# This can be expanded to handle POST webhook data from the frontend if you want

async def webhook_handler(update, context):
    # Just placeholder for now
    await update.message.reply_text("Webhook received!")
