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
		url = crycompare.Price()
		self.baseurl = url.coinList()['BaseImageUrl']
		self.coinurl = url.coinList()['Data'][coin]['ImageUrl']
	def create_image_url(self):
		return self.baseurl + self.coinurl

class Currency:
	
	def __init__(self, coin):
		self.coin = coin
		self.coinmarketcap = Market()
		self.image = Image(self.coinmarketcap.ticker(coin, limit=3)[0]['symbol'])
		#self.history = History()
	#the following functions obtain specific info from the list provided by the market object
	def value(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['price_usd']), 'n')
	def market_cap(self):
		return '{:,.2f}'.format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['market_cap_usd']))
	def percent_one_hr(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['percent_change_1h']), 'n')
	def percent_one_day(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['percent_change_24h']) , 'n')
	def percent_one_week(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['percent_change_7d']), 'n')
		#returns the correctly formatted name of the currency
	def formatted_name(self):
		return self.coinmarketcap.ticker(self.coin, limit=3)[0]['name']
	def get_image(self):
		return self.image.create_image_url()
	#def historica_data(self):
	#	return self.history.Histo

class shortCurrency:

	def __init__(self, shortcoin):
		#initialized using the cryptocompare API
		self.name = crycompare.Price()
		self.shortcoin = shortcoin
		#Uses the symbol to return the full name of the coin
		self.coin = self.name.coinList()['Data'][shortcoin]['CoinName']
		self.coinmarketcap = Market()
		self.image = Image(self.coinmarketcap.ticker(self.coin, limit=3)[0]['symbol'])
		#self.history = History()
	#the following functions obtain specific info from the list provided by the market object
	def value(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['price_usd']), 'n')
	def market_cap(self):
		return '{:,.2f}'.format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['market_cap_usd']))
	def percent_one_hr(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['percent_change_1h']), 'n')
	def percent_one_day(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['percent_change_24h']) , 'n')
	def percent_one_week(self):
		return format(float(self.coinmarketcap.ticker(self.coin, limit=3)[0]['percent_change_7d']), 'n')
	def formatted_name(self):
		return self.coinmarketcap.ticker(self.coin, limit=3)[0]['name']
	def get_image(self):
		return self.image.create_image_url()
