from bitcoin_price import BitcoinPrice
import time

price_monitor = BitcoinPrice()
# get time in sec
prev_time = time.time()
last_price_check = prev_time
current_price = 0
counter = 0
while counter < 10:
    price_list = list()
    curr_time = time.time()
    interval = curr_time - prev_time
    # check price every 60 seconds
    if interval > 10.0:
        counter = counter + 1
        current_price = price_monitor.get_current_price()
        f = open('price_data.txt', 'a')
        f.write(current_price)
        f.write('\n')
        f.close()
        prev_time = curr_time
