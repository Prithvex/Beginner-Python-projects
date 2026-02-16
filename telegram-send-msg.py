# pip install python-telegram-bot

from telegram import Bot

bot = Bot(token="YOUR_BOT_TOKEN")

chat_ids = [
    123456789,
    987654321
]

for chat_id in chat_ids:
    bot.send_message(chat_id=chat_id, text="Hello everyone!")
