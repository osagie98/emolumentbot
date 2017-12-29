import coinmarketcap
from coinmarketcap import Market
import locale
import crycompare
#allows formatting of floats
locale.setlocale(locale.LC_ALL, '')

class Currency:
	
	def __init__(self, coin):
		self.coin = coin
		self.coinmarketcap = Market()
		self.history = History()
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
	def historica_data(self):
		return self.history.Histo
