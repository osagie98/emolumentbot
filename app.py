#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from telegram.ext import Updater
from time import sleep
#to format numbers
import locale
updater = Updater(token="481020495:AAGnz18VMT21UfeM0GaifqOZsQQY9x9Etr4")
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
	#changes unicode object into a string
	querys = query.encode('utf-8')
	if not query:
		return
	if " " in querys:
		#create list with query words
		qList = querys.split()
		#create chooser object
		c = currency.Chooser(qList[0], qList[1])
		s = currency.Symbol(qList[1].upper())
		results = [
			InlineQueryResultArticle(
				id=uuid4(),
				title=c.formatted_name(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " value: $" + c.value()),
				thumb_url=c.get_image()
			),
		#value of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Value in ' + qList[1].upper(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " value: " + s.get_symbol() + " " + c.value_foreign()),
				description= s.get_symbol() + c.value_foreign()
			),
			#market cap of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Market Capitalization in ' + qList[1].upper(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " market cap: " + s.get_symbol() + " " + c.market_cap_foreign()),
				description= s.get_symbol() + c.market_cap_foreign()
			),
			#one hour percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='24 Hour Volume in ' + qList[1].upper(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " 24hr volume: " + s.get_symbol() + " " + c.day_foreign()),
				description= s.get_symbol() + c.day_foreign()
			)
		]
	else:
		#create chooser object
		c = currency.Chooser(querys)
		results = [
			InlineQueryResultArticle(
				id=uuid4(),
				title=c.formatted_name(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " value: $" + c.value()),
				thumb_url=c.get_image()
			),
		#value of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Value',
				input_message_content=InputTextMessageContent(c.formatted_name() + " value: $" + c.value()),
				description= '$' + c.value()
			),
			#market cap of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Market Capitalization',
				input_message_content=InputTextMessageContent(c.formatted_name() + " market cap: $" + c.market_cap()),
				description= '$' + c.market_cap()
			),
			#one hour percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Hour Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " one hour percent change: " + c.percent_one_hr() + '%'),
				description= c.percent_one_hr() + '%'
			),
			#one day percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Day Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " one day percent change: " + c.percent_one_day() + '%'),
				description= c.percent_one_day() + '%'
			),
			#one week percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Week Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " one week percent change: " + c.percent_one_week() + '%'),
				description= c.percent_one_week() + '%'
			),
	        InlineQueryResultArticle(
	            id=uuid4(),
	            title='Version',
	            input_message_content=InputTextMessageContent('EmolumentBot alpha v. 0.0.3 This is a barely functional bot. Release soon to follow\n\t- Update (1/4/18): Limited functionality added for supported coinmarketcap currencies. Formatting improved.'),
	            description= 'Information on the latest update.'
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
