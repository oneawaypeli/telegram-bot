from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = 7803925257:AAGLxHgAPHJYgQLcGsYgsDpl_gvT-QavGmI
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

async def start(update: Update, context):
    await update.message.reply_text("Hei! Olen Telegram-botti. Kuinka voin auttaa?")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

async def caps(update: Update, context):
    text_caps = ' '.join(context.args).upper()
    await update.message.reply_text(text_caps)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("caps", caps))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()
