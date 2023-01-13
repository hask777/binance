from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
from cred import API_KEY, SECRET_KEY

api_key = API_KEY
api_secret = SECRET_KEY

client = Client(api_key, api_secret, testnet=True)

# tickers = client.get_account()

# client.ping()

print(client.get_all_orders(symbol='BNBBTC', limit=10))
