import coinmarketcap
from coinmarketcap import Market
import locale
import crycompare

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
print coins.ticker('miota', limit=3)[0]['symbol']

coin = u"bitcoin cash / BCC"
coin = coin.replace(' ', '-')
print coin