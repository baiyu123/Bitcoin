def average(price_list):
    sum = 0
    for price in price_list:
        sum = sum + price
    return sum / price_list.size()


def sma(data, window):
    if len(data) < window:
        return None
    return sum(data[-window:]) / float(window)


def ema(data, window):
    if len(data) < 2 * window:
        raise ValueError("data is too short")
    c = 2.0 / (window + 1)
    current_ema = sma(data[-window * 2:-window], window)
    for value in data[-window:]:
        current_ema = (c * value) + ((1 - c) * current_ema)
    return current_ema
