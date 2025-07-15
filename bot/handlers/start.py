from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from database.users import add_user
from database.referrals import add_referral

async def start(update, context):
    args = context.args
    user = update.effective_user
    referred_by = None

    if args and args[0].startswith("ref_"):
        try:
            referred_by = int(args[0][4:])
            add_referral(referrer_id=referred_by, referred_id=user.id)
        except Exception:
            referred_by = None

    add_user(user.id, user.username, referred_by)

    keyboard = [
        [
            InlineKeyboardButton(
                text="Open Store",
                web_app=WebAppInfo(url=context.bot_data['WEB_APP_URL'])
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click below to open the store.", reply_markup=reply_markup)
