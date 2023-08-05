import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello {update.effective_chat.first_name}",
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def argument_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    argument = context.args
    argument_text = ' '.join(argument)
    reply_text = f"The argument provided by {update.effective_chat.first_name} is {argument_text}"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)


async def movie_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass


if __name__ == "__main__":
    token = "6064726044:AAH7J1KZPl10qRwU6iWSpkafFqSmTtpJ5bw"
    url = "https://filthy-getup-clam.cyclic.app"
    application = ApplicationBuilder().token(token).build()

    # Defining handler
    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    argument_handler = CommandHandler('argument', argument_command)

    # Adding Handler
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(argument_handler)
    application.run_webhook(listen="0.0.0.0",
                            port=8443,
                            url_path=token,
                            webhook_url=f"{url}/{token}")
    application.run_polling()