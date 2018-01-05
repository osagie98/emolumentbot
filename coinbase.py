
from telegram.ext import Updater
from time import sleep
#to format numbers
import locale
updater = Updater(token="422005629:AAGAQNWUHuRYEC8ezlTfgJfPHrvARKAu4sg")
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#start command implementation
def coinbase(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Coinbase integration complete")

from telegram.ext import CommandHandler, CallbackQueryHandler
from uuid import uuid4

#adds handler for the coinbase command
coinbase_handler = CommandHandler('coinbase', coinbase)
dispatcher.add_handler(coinbase_handler)

updater.start_polling()
updater.idle()