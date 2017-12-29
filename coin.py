import coinmarketcap
import locale
locale.setlocale(locale.LC_ALL, '')
from coinmarketcap import Market
coinmarketcap = Market()
test = coinmarketcap.ticker('bitcoin', limit=3)[0]['market_cap_usd']

test = float(test)
print '{:,.2f}'.format(test)

