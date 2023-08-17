import logging
from pyrogram import Client, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message()
def start(_, message):
    user = message.from_user
    message.reply_text(f"Hi {user.first_name}! Welcome to the game.")

@app.on_message()
def play_game(_, message):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data='1'),
         InlineKeyboardButton("Option 2", callback_data='2')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text('Choose an option:', reply_markup=reply_markup)

@app.on_callback_query()
def button_click(_, query: CallbackQuery):
    query.answer()

    if query.data == '1':
        query.edit_message_text(text="You chose Option 1!")
    elif query.data == '2':
        query.edit_message_text(text="You chose Option 2!")

if __name__ == "__main__":
    app.run()
