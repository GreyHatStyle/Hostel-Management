# Passed!!
from typing import Final
from telegram import Update
import time
import Extras
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import telegram.ext as tl
Token: Final = "your_api_key"
Bot_username: Final = 'your_bot_name'


# Commands

async def start_command(update: Update, context: tl.ContextTypes.DEFAULT_TYPE):
    s = """Hello! Please write your complain (For Plumber, Carpenter or Electrician) 
in this Format (A-101 : Plumber)\n
If you have Complain related to other issues then follow this format
(A-101 : Others : {Your Name} : {Your Complain})..."""
    await update.message.reply_text(s)


# Responses

def handle_response(text: str, date) -> str:
    check = False
    lst = list(text.split(":"))
    check = Extras.check_Message(lst, str(date))

    if check:
        return "Complain Registered"
    else:
        return "Please Type complain in mentioned Format"


async def handle_message(update: Update, context: tl.ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    data_message = f'User ({update.message.chat.id} in {message_type}: [{text}] date : [{update.message.date}]'
    date = (update.message.date).date()
    response: str = handle_response(text, date)
    print("Bot: ", response)
    await update.message.reply_text(response)


async def error(update: Update, context: tl.ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused the error {context.error}')


def main():
    print("Starting bot...")

    app = tl.Application.builder().token(Token).build()
    app.add_handler(tl.CommandHandler('start', start_command))

    # Messages
    app.add_handler(tl.MessageHandler(tl.filters.TEXT, handle_message))
    # Error
    app.add_error_handler(error)
    app.run_polling(poll_interval=3)
    #hi
