# from app.config import config
from app.config import *
# '''
#     This function will return all Exchanges supported by ccxt

# def getExchanges():
#     return ccxt.excchanges

# def createExchange(name, options):
#     exchange = eval('ccxt.' + name + '(' + str(options) + ')')    
#     return exchange

# def getPublicTrades(name, currency = 'BTC/USD'):
#     options = dict(config.getOptionsForExchange(name))
#     if(options):
#         exchange = createExchange(name, options)
#     else:
#         return {'status' : False, 'message' : 'No such Exchange is configured!'}
#     print('exchange.symbols : ', exchange.markets)
#     data = exchange.fetchTrades(symbol = currency)
#     print("data : ", data)
#     return data
    
# def getMyTrades(name, currency = 'BTC/USD'):
#     options = dict(config.getOptionsForExchange(name))
#     if(options):
#         exchange = createExchange(name, options)
#     else:
#         return {'status' : False, 'message' : 'No such Exchange is configured!'}
#     print('exchange.symbols : ', exchange.markets)
#     data = exchange.fetchTrades(symbol = currency)
#     print("data : ", data)
#     return data


# def fetchTicker(name, currency = 'BTC/USD'):
#     options = dict(config.getOptionsForExchange(name))
#     if(options):
#         exchange = createExchange(name, options)
#     else:
#         return {'status' : False, 'message' : 'No such Exchange is configured!'}
#     print('exchange.symbols : ', exchange.markets)
#     data = exchange.fetchTicker(symbol = currency)
#     print("data : ", data)
#     return data


# def fetch_balance(name):
#     options = dict(config.getOptionsForExchange(name))
#     if(options):
#         exchange = createExchange(name, options)
#     else:
#         return {'status' : False, 'message' : 'No such Exchange is configured!'}
#     print('exchange.symbols : ', exchange.markets)
#     data = exchange.fetch_balance()
#     print("data : ", data)
#     return data
#     '''