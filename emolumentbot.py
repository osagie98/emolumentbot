from telegram.ext import Updater
from time import sleep
#to format numbers
import locale
updater = Updater(token='422005629:AAGAQNWUHuRYEC8ezlTfgJfPHrvARKAu4sg')
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#start command implementation
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler, CallbackQueryHandler
from uuid import uuid4

#adds handler for the start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#simple handler to obtain bitcoin price, remove later
import coinmarketcap
from coinmarketcap import Market
def get(bot, update):
	coinmarketcap =Market()
	money = coinmarketcap.ticker('bitcoin', limit=3, convert='EUR')
	bot.send_message(chat_id=update.message.chat_id, text=money[0]['price_usd'])
	print(update.message.chat_id)
get_handler = CommandHandler('get', get)
dispatcher.add_handler(get_handler)

#libraries containing methods to handle queries and create keyboards
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup

#importing the custom currency class
import currency

def inline_currency(bot, update):

	query = update.inline_query.query
	if not query:
		return
	if 3 == 3:
		print 'yes'
	#create currency object
	c = currency.Currency(query)
	results = [
	#value of the currency
		InlineQueryResultArticle(
			id=uuid4(),
			title='VALUE: $' + c.value(),
			input_message_content=InputTextMessageContent(query.title() + " value: $" + c.value())
		),
		#market cap of the currency
		InlineQueryResultArticle(
			id=uuid4(),
			title='MARKET CAP: $' + c.market_cap(),
			input_message_content=InputTextMessageContent(query.title() + " market cap: $" + c.market_cap())
		),
		#one hour percent change of the currency
		InlineQueryResultArticle(
			id=uuid4(),
			title='1 HR PERCENT CHANGE: ' + c.percent_one_hr() + '%',
			input_message_content=InputTextMessageContent(query.title() + " one hour percent change: " + c.percent_one_hr() + '%')
		),
		#one day percent change of the currency
		InlineQueryResultArticle(
			id=uuid4(),
			title='1 DAY PERCENT CHANGE: ' + c.percent_one_day() + '%',
			input_message_content=InputTextMessageContent(query.title() + " one day percent change: " + c.percent_one_day() + '%')
		),
		#one week percent change of the currency
		InlineQueryResultArticle(
			id=uuid4(),
			title='1 WEEK PERCENT CHANGE: ' + c.percent_one_week() + '%',
			input_message_content=InputTextMessageContent(query.title() + " one week percent change: " + c.percent_one_week() + '%')
		),
        InlineQueryResultArticle(
            id=uuid4(),
            title='VERSION',
            input_message_content=InputTextMessageContent('Emolumentbot v. 0.0. This is a non-functional bot. Release soon to follow'),
        )
	]
	
	bot.answer_inline_query(update.inline_query.id, results)

#libraries containing methods to handle errors
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)


#this function handles all possible errors and prints to console
def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        # remove update.message.chat_id from conversation list
        print('Unauthorized Error')
    except BadRequest:
        # handle malformed requests - read more below!
        print('BadRequest Error')
        print(error)
    except TimedOut:
        # handle slow connection problems
        print('TimedOut Error')
    except NetworkError:
        # handle other connection problems
        print('Netowrk Error')
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        print('ChatMigrated Error')
    except TelegramError:
        # handle all other telegram related errors
        print('Telegram Error')


from telegram.ext import InlineQueryHandler

inline_currency_handler = InlineQueryHandler(inline_currency)
dispatcher.add_handler(inline_currency_handler)
dispatcher.add_error_handler(error_callback)

updater.start_polling()
updater.idle()