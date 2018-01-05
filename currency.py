#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import coinmarketcap
from coinmarketcap import Market
import locale
import crycompare
import gdax
#allows formatting of floats
locale.setlocale(locale.LC_ALL, '')

class Image:
	def __init__(self, coin):
		#Special case for IOTA, FIX WITH A DIFFERENT API OR WEBSCRAPING
		if coin == 'MIOTA':
			coin = 'IOT'
		self.urlDict = crycompare.Price().coinList()
		self.baseurl = self.urlDict['BaseImageUrl']
		self.coinurl = self.urlDict['Data'][coin]['ImageUrl']
	def create_image_url(self):
		return self.baseurl + self.coinurl

class Currency:
	
	def __init__(self, coin, currency):
		self.coin = coin
		self.coinmarketcap = Market()
		self.currency = currency
		if currency == '':
			self.coinDict = self.coinmarketcap.ticker(self.coin)[0]
		else:
			self.coinDict = self.coinmarketcap.ticker(self.coin, convert=currency)[0]
		self.image = Image(self.coinDict['symbol'])
		#self.history = History()
	#the following functions obtain specific info from the list provided by the market object
	def value(self):
		return format(float(self.coinDict['price_usd']), 'n')
	def market_cap(self):
		return '{:,.2f}'.format(float(self.coinDict['market_cap_usd']))
	def percent_one_hr(self):
		return format(float(self.coinDict['percent_change_1h']), 'n')
	def percent_one_day(self):
		return format(float(self.coinDict['percent_change_24h']) , 'n')
	def percent_one_week(self):
		return format(float(self.coinDict['percent_change_7d']), 'n')
	def day(self):
		return '{:,.2f}'.format(float(self.coinDict['24h_volume_usd']), 'n')
		#returns the correctly formatted name of the currency
	def formatted_name(self):
		return self.coinDict['name']
	def get_image(self):
		return self.image.create_image_url()
	def value_foreign(self):
		return '{:,.2f}'.format(float(self.coinDict['price_' + self.currency.lower()]), 'n')
	def day_foreign(self):
		return '{:,.2f}'.format(float(self.coinDict['24h_volume_' + self.currency.lower()]), 'n')
	def market_cap_foreign(self):
		return '{:,.2f}'.format(float(self.coinDict['market_cap_' + self.currency.lower()]), 'n')
	#def historica_data(self):
	#	return self.history.Histo

class shortCurrency:

	def __init__(self, shortcoin, currency):
		#initialized using the cryptocompare API
		self.name = crycompare.Price()
		self.shortcoin = shortcoin
		self.currency = currency
		#Special case for IOTA, FIX WITH A DIFFERENT API OR WEBSCRAPING
		if shortcoin == 'MIOTA':
			self.shortcoin = 'IOT'
		#Uses the symbol to return the full name of the coin
		self.coin = self.name.coinList()['Data'][self.shortcoin]['CoinName']
		self.coin = self.coin.replace(' ', '-')
		self.coinmarketcap = Market()
		if currency == '':
			self.coinDict = self.coinmarketcap.ticker(self.coin)[0]
		else:
			self.coinDict = self.coinmarketcap.ticker(self.coin, convert=currency)[0]
		self.image = Image(self.coinDict['symbol'])
		#self.history = History()
	#the following functions obtain specific info from the list provided by the market object
	def value(self):
		return format(float(self.coinDict['price_usd']), 'n')
	def market_cap(self):
		return '{:,.2f}'.format(float(self.coinDict['market_cap_usd']))
	def percent_one_hr(self):
		return format(float(self.coinDict['percent_change_1h']), 'n')
	def percent_one_day(self):
		return format(float(self.coinDict['percent_change_24h']) , 'n')
	def percent_one_week(self):
		return format(float(self.coinDict['percent_change_7d']), 'n')
	def day(self):
		return '{:,.2f}'.format(float(self.coinDict['24h_volume_usd']), 'n')
	def formatted_name(self):
		return self.coinDict['name']
	def get_image(self):
		return self.image.create_image_url()
	def value_foreign(self):
		return '{:,.2f}'.format(float(self.coinDict['price_' + self.currency.lower()]), 'n')
	def day_foreign(self):
		return '{:,.2f}'.format(float(self.coinDict['24h_volume_' + self.currency.lower()]), 'n')
	def market_cap_foreign(self):
		return '{:,.2f}'.format(float(self.coinDict['market_cap_' + self.currency.lower()]), 'n')

#a class that decides whether query is the full name of the coin, or a symbol, and creates the correct class
class Chooser:

	def __init__(self, query, currency=''):
		self.check = Market()
		self.coinDict = self.check.ticker(limit=1000)
		#uppercase for symbols
		query2 = query.upper()
		for x in range(0, len(self.coinDict)-1):
			if query == self.coinDict[x]['id'] or query == self.coinDict[x]['name']:
				self.money = Currency(query, currency)
				break
			if query2 == self.coinDict[x]['symbol']:
				self.money = shortCurrency(query2, currency)
				break
	#the following functions return values from either the Currency or shortCurrency class
	def value(self):
		return self.money.value()
	def market_cap(self):
		return self.money.market_cap()
	def percent_one_hr(self):
		return self.money.percent_one_hr()
	def percent_one_day(self):
		return self.money.percent_one_day()
	def percent_one_week(self):
		return self.money.percent_one_week()
	def day(self):
		return self.money.day()
	def formatted_name(self):
		return self.money.formatted_name()
	def get_image(self):
		return self.money.get_image()
	def value_foreign(self):
		return self.money.value_foreign()
	def day_foreign(self):
		return self.money.day_foreign()
	def market_cap_foreign(self):
		return self.money.market_cap_foreign()

#A class for GDAX information
class Gdax:

	def __init__(self):
		self.dax = gdax.PublicClient()
		self.btc = self.dax.get_product_ticker(product_id='BTC-USD')
		self.ltc = self.dax.get_product_ticker(product_id='LTC-USD')
		self.eth = self.dax.get_product_ticker(product_id='ETH-USD')
		self.bch = self.dax.get_product_ticker(product_id='BCH-USD')
	def get_btc(self):
		return format(float(self.btc['price']), 'n')
	def get_ltc(self):
		return format(float(self.ltc['price']), 'n')
	def get_eth(self):
		return format(float(self.eth['price']), 'n')
	def get_bch(self):
		return format(float(self.bch['price']), 'n')
	def get_btc_vol(self):
		return format(float(self.btc['volume']), 'n')
	def get_ltc_vol(self):
		return format(float(self.ltc['volume']), 'n')
	def get_eth_vol(self):
		return format(float(self.eth['volume']), 'n')
	def get_bch_vol(self):
		return format(float(self.bch['volume']), 'n')

#A class that returns supported currency symbols
class Symbol:
	#Solve unicode issue for KRW and RUB
	def __init__(self, sign):
		self.signDict = {'USD':'$', 'AUD':'AU$', 'BRL':'R$', 'CAN':'C$', 
		'CHF':'CHF ', 'CNY':'C¥', 'EUR':'€', 'GBP':'£', 'HKD':'HK$', 
		'IDR':'Rp ', 'JPY':'JP¥', 'KRW':'W', 'MXN':'MX$', 'RUB':'P', 'TEST':''}
		self.sign = sign
	def get_symbol(self):
		#placeholder till encoding is fixed
		return self.signDict['TEST']