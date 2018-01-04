#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import coinmarketcap
from coinmarketcap import Market
import locale
import crycompare
import babel
import feedparser

d = feedparser.parse('http://feeds.feedburner.com/Coindesk?format=xml')
print d['entries'][1]['summary_detail']['value'] 

'''
signDict = {'USD':'$', 'AUD':'AU$', 'BRL':'R$', 'CAN':'C$', 
		'CHF':'CHF ', 'CNY':'C¥', 'EUR':'€', 'GBP':'£', 'HKD':'HK$', 
		'IDR':'Rp ', 'JPY':'JP¥', 'KRW':'₩', 'MXN':'MX$', 'RUB':'₽'}
print signDict['RUB']
'''
'''
locale.setlocale(locale.LC_ALL, '')
from coinmarketcap import Market
coinmarketcap = Market()
test = coinmarketcap.ticker('bitcoin', limit=3)[0]['market_cap_usd']

test = float(test)
print '{:,.2f}'.format(test)
'''
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
print check.ticker(limit=3, convert='eur')
query = 'putincoin'
query2 = query.upper()
for x in range(0, len(check.ticker())-1):
	if query == check.ticker()[x]['id'] or query == check.ticker()[x]['name']:
		print 'This is the full name'
		break
	if query2 == check.ticker()[x]['symbol']:
		print 'This is a symbol'
		break


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