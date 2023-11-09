# Passed!!
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token: Final = "6461982132:AAFTBNN4DqEb-hG6gxoY7zyr83CJ88JVqgk"
Bot_username: Final = '@manas_hos_bot'


# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello please Write your complain in (Room no. : Complain field) format\nEg: B-04 "
                                    ": Plumber")


# Responses

def handle_response(text: str) -> str:
    if ':' in text:
        return "Complain Registered!"
    else:
        return "Incomplete information"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id} in {message_type}: [{text}]')

    response: str = handle_response(text)
    print("Bot: ", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused the error {context.error}')


print("Starting bot...")
app = Application.builder().token(Token).build()
app.add_handler(CommandHandler('start', start_command))

# Messages
app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Error
app.add_error_handler(error)
print("Polling...")
app.run_polling(poll_interval=3)
