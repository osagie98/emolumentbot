import coinmarketcap
from coinmarketcap import Market
import locale
import crycompare
import config

'''
locale.setlocale(locale.LC_ALL, '')
from coinmarketcap import Market
coinmarketcap = Market()
test = coinmarketcap.ticker('bitcoin', limit=3)[0]['market_cap_usd']

test = float(test)
print '{:,.2f}'.format(test)
'''

test = crycompare.Price()
#print test.coinList()['Data']['BCH']

test2 = crycompare.Price()
print test2.price('BTC', 'USD')['USD']


coins = Market()

query = 'bitcoin'
for x in range(0, len(coins.ticker(limit=3)) -1):
	if query == coins.ticker(limit=3)[x]['name']:
		print '##############'

coin = u"bitcoin cash / BCC"
coin = coin.replace(' ', '-')
print coin

check = Market()
print config.obnoxious_token
query = 'putincoin'
query2 = query.upper()
for x in range(0, len(check.ticker())-1):
	if query == check.ticker()[x]['id'] or query == check.ticker()[x]['name']:
		print 'This is the full name'
		break
	if query2 == check.ticker()[x]['symbol']:
		print 'This is a symbol'
		break

'''
		self.check = Market()
		#creates lists of possible queries
		idList = []
		nameList = []
		symbolList = []
		for x in range(0, len(self.check.ticker())-1):
			idList.append(self.check.ticker()[x]['id'])
			nameList.append(self.check.ticker()[x]['name'])
			symbolList.append(self.check.ticker()[x]['symbol'])
		#uppercase for symbols
		query2 = query.upper()
		for y in range(0, len(idList) -1):
			if query == idList[y] or query == nameList[y]:
				print 'I GOT HERE'
				self.money = Currency(query)
				break
			if query2 == symbolList[y]:
				self.money = shortCurrency(query2)
				break
'''	