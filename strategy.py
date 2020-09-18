import logging
from kiteconnect import KiteTicker
import threading

logging.basicConfig(level=logging.DEBUG)
api_key="key"
api_secret="secret"
access_token=""

def place_order(transaction_type,trading_symbol,trigger_price):
	kite.order_place(trading_symbol="COmpany Name/Put Option token",exchange="NSE",quantity=25,transaction_type=transaction_type,order_type="MARKET",triger_price=22507,stoploss=20)


kws=KiteTicker(api_key,access_token)
def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([738561, 5633])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_LTP, [738561])
    if RELIANCE["ltp"]==22704:  # Taken from excel given
    	triger_price=22507
    	trading_symbol="RELIANCE SEP 2200 CE" #put/call token
    	transaction_type="BUY"
    	t1=threading.Thread(target=place_order,args=[transaction_type,trigger_price,trading_symbol])
    	trading_symbol="RELIANCE 2200 PE"
    	t2=threading.Thread(target=place_order,args=[transaction_type,trigger_price,trading_symbol])
    	t1.start()
    	t2.start()
    if RELIANCE["ltp"]==21604:   # Taken from excel given
    	triger_price=21792
    	
    	trading_symbol="RELIANCE SEP 2200 CE" #put/call token
    	transaction_type="SELL"
    	t1=threading.Thread(target=place_order,args=[transaction_type,trigger_price,trading_symbol])
    	trading_symbol="RELIANCE 2200 PE"
    	t2=threading.Thread(target=place_order,args=[transaction_type,trigger_price,trading_symbol])
    	t1.start()
    	t2.start()


def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect(threaded=True)

