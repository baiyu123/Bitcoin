from bitcoin_price import BitcoinPrice
from database import PriceDatabase
from math_utils import average, ema, sma
from sms import SMSManager
import time

price_monitor = BitcoinPrice()
price_database = PriceDatabase()
# price_database.connect_database('prices.db')
# price_database.create_price_table()
# get time in sec
prev_time = time.time()
last_price_check = prev_time
current_price = 0
# 1 mins price check

# sms
manager = SMSManager()

current_price = 0
hour_avg = 0
twenty_min_avg = 0
prev_hour_diff_six = 0
hour_diff_six = 0
while True:
    curr_time = time.time()
    interval = curr_time - prev_time
    # check price every 60 seconds
    if interval > 1.0:
        price_database.connect_database('prices.db')
        current_price = price_database.get_latest_available()
        twenty_min_avg = ema(price_database.get_last_items(20 * 2), 20)
        hour_avg = ema(price_database.get_last_items(60 * 2), 60)
        hour_diff_six = twenty_min_avg - hour_avg
        if prev_hour_diff_six * hour_diff_six < 0:
            # cross over occur
            if hour_diff_six < 0:
                # sell signal
                manager.send_message('Sell', '+12134482436')
                print "Sell"
            if hour_diff_six > 0:
                # buy signal
                manager.send_message('Buy', '+12134482436')
                print "Buy"
        if hour_diff_six == 0:
            if prev_hour_diff_six < 0:
                # buy signal
                manager.send_message('Buy', '+12134482436')
                print "Buy"
            if prev_hour_diff_six > 0:
                # sell signal
                manager.send_message('Sell', '+12134482436')
                print "Sell"
        prev_time = curr_time
        prev_hour_diff_six = hour_diff_six
        price_database.close()
