import coinmarketcap
from coinmarketcap import Market
import locale
import crycompare
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
	
	def __init__(self, coin):
		self.coin = coin
		self.coinmarketcap = Market()
		self.coinDict = self.coinmarketcap.ticker(self.coin)[0]
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
		#returns the correctly formatted name of the currency
	def formatted_name(self):
		return self.coinDict['name']
	def get_image(self):
		return self.image.create_image_url()
	#def historica_data(self):
	#	return self.history.Histo

class shortCurrency:

	def __init__(self, shortcoin):
		#initialized using the cryptocompare API
		self.name = crycompare.Price()
		self.shortcoin = shortcoin
		#Special case for IOTA, FIX WITH A DIFFERENT API OR WEBSCRAPING
		if shortcoin == 'MIOTA':
			self.shortcoin = 'IOT'
		#Uses the symbol to return the full name of the coin
		self.coin = self.name.coinList()['Data'][self.shortcoin]['CoinName']
		self.coin = self.coin.replace(' ', '-')
		self.coinmarketcap = Market()
		self.coinDict = self.coinmarketcap.ticker(self.coin)[0]
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
	def formatted_name(self):
		return self.coinDict['name']
	def get_image(self):
		return self.image.create_image_url()

#a class that decides whether query is the full name of the coin, or a symbol, and creates the correct class
class Chooser:

	def __init__(self, query):
		self.check = Market()
		self.coinDict = self.check.ticker(limit=1000)
		#uppercase for symbols
		query2 = query.upper()
		for x in range(0, len(self.coinDict)-1):
			if query == self.coinDict[x]['id'] or query == self.coinDict[x]['name']:
				self.money = Currency(query)
				break
			if query2 == self.coinDict[x]['symbol']:
				self.money = shortCurrency(query2)
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
	def formatted_name(self):
		return self.money.formatted_name()
	def get_image(self):
		return self.money.get_image()