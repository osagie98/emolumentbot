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
	''' 
	button17 = InlineKeyboardButton('2017', callback_data='2017')
	button16 = InlineKeyboardButton('2016', callback_data='2016')
	button15 = InlineKeyboardButton('2015', callback_data='2015')
	button14 = InlineKeyboardButton('2014', callback_data='2014')
	button13 = InlineKeyboardButton('2013', callback_data='2013')
	button12 = InlineKeyboardButton('2012', callback_data='2012')
	test2 = [button17, button16, button15]
	test3 = [button14, button13, button12]
	test4 = [test2, test3]
	test5 = InlineKeyboardMarkup(test4)
	'''

	#buttons for the inline keyboard
	button17 = KeyboardButton('2017', callback_data='2017')
	button16 = KeyboardButton('2016', callback_data='2016')
	button15 = KeyboardButton('2015', callback_data='2015')
	button14 = KeyboardButton('2014', callback_data='2014')
	button13 = KeyboardButton('2013', callback_data='2013')
	button12 = KeyboardButton('2012', callback_data='2012')
	test2 = [button17, button16, button15]
	test3 = [button14, button13, button12]
	test4 = [test2, test3]

	#creating the custom keyboard
	test5 = ReplyKeyboardMarkup(test4)
	query = update.inline_query.query
	if not query:
		return
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
		#testing keyboard for historical information
		InlineQueryResultArticle(
			id=uuid4(),
			title='HISTORICAL VALUE',
			input_message_content=InputTextMessageContent('Please select a year'),
			reply_markup=test5
		)
	]
	
	bot.answer_inline_query(update.inline_query.id, results)

def button(bot, update):
	#printing the callback_query for testing, remove later
	print(update.callback_query.id)

	#creates all the buttons pertaining to the month
	buttonjan = InlineKeyboardButton('Jan.', callback_data='1')
	buttonfeb = InlineKeyboardButton('Feb.', callback_data='2')
	buttonmar = InlineKeyboardButton('Mar.', callback_data='3')
	buttonapr = InlineKeyboardButton('Apr.', callback_data='4')
	buttonmay = InlineKeyboardButton('May.', callback_data='5')
	buttonjun = InlineKeyboardButton('Jun.', callback_data='6')
	buttonjul = InlineKeyboardButton('Jul.', callback_data='7')
	buttonaug = InlineKeyboardButton('Aug.', callback_data='8')
	buttonsep = InlineKeyboardButton('Sep.', callback_data='9')
	buttonoct = InlineKeyboardButton('Oct.', callback_data='10')
	buttonnov = InlineKeyboardButton('Nov.', callback_data='11')
	buttondec = InlineKeyboardButton('Dec.', callback_data='12')

	monthcol1 = [buttonjan, buttonfeb, buttonmar, buttonapr]
	monthcol2 = [buttonmay, buttonjun, buttonjul, buttonaug]
	monthcol3 = [buttonsep, buttonoct, buttonnov, buttondec]
	#establishes the keyboard
	allmonth = InlineKeyboardMarkup([monthcol1, monthcol2, monthcol3])

	#prints to check if message information has changed, remove later
	theid = update.callback_query
	print(theid)
	
 	#responds to the inlinequery response
 	#bot.edit_message_reply_markup(inline_message_id=update.callback_query.inline_message_id, reply_markup=allmonth)
 	#theid2 = update.callback_query
 	#print(theid2)
 	testmessage = bot.send_message(chat_id=update.callback_query.chat_instance, text='Please select a month', reply_markup=allmonth)
 	print(testmessage)
 	'''
 	button01 = InlineKeyboardButton('1', callback_data='01')
 	button02 = InlineKeyboardButton('2', callback_data='02')
 	button03 = InlineKeyboardButton('3', callback_data='03')
 	button04 = InlineKeyboardButton('4', callback_data='04')
 	button05 = InlineKeyboardButton('5', callback_data='05')
 	button06 = InlineKeyboardButton('6', callback_data='06')
 	button07 = InlineKeyboardButton('7', callback_data='07')
 	button08 = InlineKeyboardButton('8', callback_data='08')
 	button09 = InlineKeyboardButton('9', callback_data='09')
 	button10 = InlineKeyboardButton('10', callback_data='10')
 	button11 = InlineKeyboardButton('11', callback_data='11')
 	button12 = InlineKeyboardButton('12', callback_data='12')
 	button13 = InlineKeyboardButton('13', callback_data='13')
 	button14 = InlineKeyboardButton('14', callback_data='14')
 	button15 = InlineKeyboardButton('15', callback_data='15')
 	button16 = InlineKeyboardButton('16', callback_data='16')
 	button17 = InlineKeyboardButton('17', callback_data='17')
 	button18 = InlineKeyboardButton('18', callback_data='18')
 	button19 = InlineKeyboardButton('19', callback_data='19')
 	button20 = InlineKeyboardButton('20', callback_data='20')
 	button21 = InlineKeyboardButton('21', callback_data='21')
 	button22 = InlineKeyboardButton('22', callback_data='22')
 	button23 = InlineKeyboardButton('23', callback_data='23')
 	button24 = InlineKeyboardButton('24', callback_data='24')
 	button25 = InlineKeyboardButton('25', callback_data='25')
 	button26 = InlineKeyboardButton('26', callback_data='26')
 	button27 = InlineKeyboardButton('27', callback_data='27')
 	button28 = InlineKeyboardButton('28', callback_data='28')
 	button29 = InlineKeyboardButton('29', callback_data='29')
 	button30 = InlineKeyboardButton('30', callback_data='30')
 	button31 = InlineKeyboardButton('31', callback_data='31')

 	numrow1 = [button01, button02, button03, button04, button05, button06, button07, button08]
 	numrow2 = [button09, button10, button11, button12, button13, button14, button15, button16]
 	numrow3 = [button17, button18, button19, button20, button21, button22, button23, button24]
 	numrow4 = [button25, button26, button27, button28, button29, button30, button31]
 	allnum = InlineKeyboardMarkup([numrow1, numrow2, numrow3, numrow4])

 	theid = update.callback_query.id
 
 	bot.edit_message_text(inline_message_id=update.callback_query.inline_message_id, text='Please select a day', reply_markup=allnum)
 	
 	bot.edit_message_text(inline_message_id=update.callback_query.inline_message_id, text='Value will go here')
 '''	
'''
def button2(bot, update):
 	button01 = InlineKeyboardButton('1', callback_data='01')
 	button02 = InlineKeyboardButton('2', callback_data='02')
 	button03 = InlineKeyboardButton('3', callback_data='03')
 	button04 = InlineKeyboardButton('4', callback_data='04')
 	button05 = InlineKeyboardButton('5', callback_data='05')
 	button06 = InlineKeyboardButton('6', callback_data='06')
 	button07 = InlineKeyboardButton('7', callback_data='07')
 	button08 = InlineKeyboardButton('8', callback_data='08')
 	button09 = InlineKeyboardButton('9', callback_data='09')
 	button10 = InlineKeyboardButton('10', callback_data='10')
 	button11 = InlineKeyboardButton('11', callback_data='11')
 	button12 = InlineKeyboardButton('12', callback_data='12')
 	button13 = InlineKeyboardButton('13', callback_data='13')
 	button14 = InlineKeyboardButton('14', callback_data='14')
 	button15 = InlineKeyboardButton('15', callback_data='15')
 	button16 = InlineKeyboardButton('16', callback_data='16')
 	button17 = InlineKeyboardButton('17', callback_data='17')
 	button18 = InlineKeyboardButton('18', callback_data='18')
 	button19 = InlineKeyboardButton('19', callback_data='19')
 	button20 = InlineKeyboardButton('20', callback_data='20')
 	button21 = InlineKeyboardButton('21', callback_data='21')
 	button22 = InlineKeyboardButton('22', callback_data='22')
 	button23 = InlineKeyboardButton('23', callback_data='23')
 	button24 = InlineKeyboardButton('24', callback_data='24')
 	button25 = InlineKeyboardButton('25', callback_data='25')
 	button26 = InlineKeyboardButton('26', callback_data='26')
 	button27 = InlineKeyboardButton('27', callback_data='27')
 	button28 = InlineKeyboardButton('28', callback_data='28')
 	button29 = InlineKeyboardButton('29', callback_data='29')
 	button30 = InlineKeyboardButton('30', callback_data='30')
 	button31 = InlineKeyboardButton('31', callback_data='31')

 	numrow1 = [button01, button02, button03, button04, button05, button06, button07, button08]
 	numrow2 = [button09, button10, button11, button12, button13, button14, button15, button16]
 	numrow3 = [button17, button18, button19, button20, button21, button22, button23, button24]
 	numrow4 = [button25, button26, button27, button28, button29, button30, button31]
 	allnum = InlineKeyboardMarkup([numrow1, numrow2, numrow3, numrow4])

 	bot.edit_message_reply_markup(inline_message_id=update.callback_query.inline_message_id, reply_markup=allnum)

def button3(bot, update):
 	bot.edit_message_text(inline_message_id=update.callback_query.inline_message_id, text='Value will go here')
'''

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
#button_handler = CallbackQueryHandler(button)
#dispatcher.add_handler(button_handler)
#button2_handler = CallbackQueryHandler(button2)
#dispatcher.add_handler(button2_handler)
#button3_handler = CallbackQueryHandler(button3)
#dispatcher.add_handler(button3_handler)
dispatcher.add_error_handler(error_callback)

updater.start_polling()
updater.idle()