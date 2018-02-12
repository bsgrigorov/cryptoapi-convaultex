from coinmarketcap import Market

coinmarketcap = Market()
coinmarketcap.ticker(start=0, limit=3, convert='USD')

a = coinmarketcap.ticker(start=0, limit=2, convert='USD')
btc_market_cap = a[0]["market_cap_usd"].encode("utf-8")