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
# 5 mins price check


def average(price_list):
    sum = 0
    for price in price_list:
        sum = sum + price
    return sum / price_list.size()
current_price = 0
six_hour_avg = 0
hour_avg = 0
prev_hour_diff_six = 0
while True:
    curr_time = time.time()
    interval = curr_time - prev_time
    # check price every 60 seconds
    if interval > 60.0:
        price_database.connect_database('prices.db')
        current_price = price_database.get_latest_available()
        hour_avg = average(price_database.get_last_items(60))
        six_hour_avg = average(price_database.get_last_items(60 * 6))
        hour_diff_six = hour_avg - six_hour_avg
        if prev_hour_diff_six * hour_diff_six < 0:
            # cross over occur
            if hour_diff_six < 0:
                # sell signal
                print "Sell"
            if hour_diff_six > 0:
                # buy signal
                print "Buy"
        prev_time = curr_time
        price_database.close()
