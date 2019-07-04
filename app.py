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
	coinmarketcap = Market()
	money = coinmarketcap.ticker('bitcoin', limit=3, convert='EUR')
	bot.send_message(chat_id=update.message.chat_id, text=money[0]['price_usd'])
	print(update.message.chat_id)
get_handler = CommandHandler('get', get)
dispatcher.add_handler(get_handler)

#libraries containing methods to handle queries and create keyboards
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup

#importing the custom currency class
import currency
import feedparser

def inline_currency(bot, update):

	query = update.inline_query.query
	#changes unicode object into a string
	#querys = query.encode('utf-8')
	querys = query
	#queryn checks for a news query
	queryn = querys.lower()
	if not query:
		#create GDAX object
		g = currency.Gdax()
		results = [
				InlineQueryResultArticle(
				id=uuid4(),
				title='GDAX',
				input_message_content=InputTextMessageContent('Bitcoin GDAX Value: $' + g.get_btc() + '\nLitecoin GDAX Value: $' + g.get_ltc() + '\nEthereum GDAX Value: $' + g.get_eth() + '\nBitcoin Cash GDAX Value: $' + g.get_bch()),
				description='View coins...',
				thumb_url='https://i.imgur.com/DQ64TdCl.jpg'
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title='Bitcoin (BTC)',
				input_message_content=InputTextMessageContent('Bitcoin GDAX Value: $' + g.get_btc() + '\nGDAX 24hr Volume: $' + g.get_btc_vol()),
				description='$' + g.get_btc(),
				thumb_url='https://www.cryptocompare.com/media/19633/btc.png'
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title='Litecoin (LTC)',
				input_message_content=InputTextMessageContent('Litecoin GDAX Value: $' + g.get_ltc() + '\nGDAX 24hr Volume: $' + g.get_ltc_vol()),
				description='$' + g.get_ltc(),
				thumb_url='https://www.cryptocompare.com/media/19782/litecoin-logo.png'
			),
		#value of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Ethereum (ETH)',
				input_message_content=InputTextMessageContent('Ethereum GDAX Value: $' + g.get_eth() + '\nGDAX 24hr Volume: $' + g.get_eth_vol()),
				description= '$' + g.get_eth(),
				thumb_url='https://www.cryptocompare.com/media/20646/eth_logo.png'
			),
			#market cap of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Bitcoin Cash (BCH)',
				input_message_content=InputTextMessageContent('Bitcoin Cash GDAX Value: $' + g.get_bch() + '\nGDAX 24hr Volume: $' + g.get_bch_vol()),
				description='$' + g.get_bch(),
				thumb_url='https://www.cryptocompare.com/media/1383919/bch.jpg'
			)
			#one hour percent change of the currency
		]
	elif queryn == 'news':
		#create feedparser object 
		d = feedparser.parse('http://feeds.feedburner.com/Coindesk?format=xml') 
		results = [
		#top feed results
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][0]['title'],
				input_message_content=InputTextMessageContent(d['entries'][0]['link']),
				description=d['entries'][0]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][1]['title'],
				input_message_content=InputTextMessageContent(d['entries'][1]['link']),
				description=d['entries'][1]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][2]['title'],
				input_message_content=InputTextMessageContent(d['entries'][2]['link']),
				description=d['entries'][2]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][3]['title'],
				input_message_content=InputTextMessageContent(d['entries'][3]['link']),
				description=d['entries'][3]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][4]['title'],
				input_message_content=InputTextMessageContent(d['entries'][4]['link']),
				description=d['entries'][4]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][5]['title'],
				input_message_content=InputTextMessageContent(d['entries'][5]['link']),
				description=d['entries'][5]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][6]['title'],
				input_message_content=InputTextMessageContent(d['entries'][6]['link']),
				description=d['entries'][6]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][7]['title'],
				input_message_content=InputTextMessageContent(d['entries'][7]['link']),
				description=d['entries'][7]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][8]['title'],
				input_message_content=InputTextMessageContent(d['entries'][8]['link']),
				description=d['entries'][8]['summary_detail']['value']
			),
			InlineQueryResultArticle(
				id=uuid4(),
				title=d['entries'][9]['title'],
				input_message_content=InputTextMessageContent(d['entries'][9]['link']),
				description=d['entries'][9]['summary_detail']['value']
			)
		]
	elif queryn == 'version':
		results = [
			InlineQueryResultArticle(
	            id=uuid4(),
	            title='Version',
	            input_message_content=InputTextMessageContent('EmolumentBot beta v. 0.0.1 This is a barely functional bot. Release soon to follow\n\t- Update (1/4/18): GDAX functionality added, Version moved, updated some icons'),
	            description= 'Information on the latest update.',
	            thumb_url='http://freevector.co/wp-content/uploads/2013/02/9788-double-wrench1.png'
			)
	    ]	
	elif ' ' in querys:
		#create list with query words
		qList = querys.split()
		#create chooser object
		c = currency.Chooser(qList[0], qList[1])
		s = currency.Symbol(qList[1].upper())
		results = [
			InlineQueryResultArticle(
				id=uuid4(),
				title=c.formatted_name(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " Value: $" + c.value()),
				thumb_url=c.get_image()
			),
		#value of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Value in ' + qList[1].upper(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " Value: " + s.get_symbol() + " " + c.value_foreign()),
				description= s.get_symbol() + c.value_foreign(),
				thumb_url='https://i.imgur.com/38v6W37l.jpg'
			),
			#market cap of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Market Capitalization in ' + qList[1].upper(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " Market Cap: " + s.get_symbol() + " " + c.market_cap_foreign()),
				description= s.get_symbol() + c.market_cap_foreign()
			),
			#24 hr volume of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='24 Hour Volume in ' + qList[1].upper(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " 24hr Volume: " + s.get_symbol() + " " + c.day_foreign()),
				description= s.get_symbol() + c.day_foreign()
			),
			#one hour percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Hour Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " One Hour Percent Change: " + c.percent_one_hr() + '%'),
				description= c.percent_one_hr() + '%'
			),
			#one day percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Day Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " One Day Percent Change: " + c.percent_one_day() + '%'),
				description= c.percent_one_day() + '%'
			),
			#one week percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Week Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " One Week Percent Change: " + c.percent_one_week() + '%'),
				description= c.percent_one_week() + '%'
			)
		]
	else:
		#create chooser object
		c = currency.Chooser(querys)
		results = [
			InlineQueryResultArticle(
				id=uuid4(),
				title=c.formatted_name(),
				input_message_content=InputTextMessageContent(c.formatted_name() + " Value: $" + c.value()),
				thumb_url=c.get_image()
			),
		#value of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Value',
				input_message_content=InputTextMessageContent(c.formatted_name() + " Value: $" + c.value()),
				description= '$' + c.value(),
				thumb_url='https://i.imgur.com/38v6W37l.jpg'
			),
			#market cap of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='Market Capitalization',
				input_message_content=InputTextMessageContent(c.formatted_name() + " Market Cap: $" + c.market_cap()),
				description= '$' + c.market_cap()
			),
			#24 hr volume of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='24 Hour Volume',
				input_message_content=InputTextMessageContent(c.formatted_name() + " 24hr Volume: $" + c.day()),
				description= '$' + c.day()
			),
			#one hour percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Hour Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " One Hour Percent Change: " + c.percent_one_hr() + '%'),
				description= c.percent_one_hr() + '%'
			),
			#one day percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Day Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " One Day Percent Change: " + c.percent_one_day() + '%'),
				description= c.percent_one_day() + '%'
			),
			#one week percent change of the currency
			InlineQueryResultArticle(
				id=uuid4(),
				title='1 Week Percent Change',
				input_message_content=InputTextMessageContent(c.formatted_name() + " One Week Percent Change: " + c.percent_one_week() + '%'),
				description= c.percent_one_week() + '%'
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
