from bitcoin_price import BitcoinPrice
from database import PriceDatabase
import time

price_monitor = BitcoinPrice()
price_database = PriceDatabase()
# price_database.connect_database('prices.db')
# price_database.create_price_table()
# get time in sec
prev_time = time.time()
last_price_check = prev_time
current_price = 0
counter = 0
# 5 mins price check

while True:
    curr_time = time.time()
    interval = curr_time - prev_time
    # check price every 60 seconds
    if interval > 1.0:
        price_database.connect_database('prices.db')
        counter = counter + 1
        current_price = price_monitor.get_current_price()
        price_database.save_price(int(curr_time), current_price)
        print str(int(curr_time)) + ': ' + str(price_database.get_price(int(curr_time)))
        prev_time = curr_time
        price_database.close()
