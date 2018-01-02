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

#test = crycompare.Price()
#print test.coinList()['Data']['BCH']['CoinName']

test2 = crycompare.Price()
print test2.price('BTC', 'USD')['USD']

coins = Market()
print coins.ticker('bitcoin-cash', limit=3)[0]['price_usd']