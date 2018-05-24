import sqlite3


class PriceDatabase:
    conn = None
    database = ''

    def __init__(self):
        pass

    # connect to data base
    def connect_database(self, database):
        self.conn = sqlite3.connect(database)
        self.database = database

    # create price table
    def create_price_table(self):
        if self.conn is None:
            return
        with self.conn:
            c = self.conn.cursor()
            c.execute("""CREATE TABLE prices(time INTEGER, price REAL)""")

    # save price and time stamp to database
    def save_price(self, time, price):
        if self.conn is None:
            return
        with self.conn:
            c = self.conn.cursor()
            c.execute("INSERT INTO prices VALUES (?, ?)",
                      (time, price))

    # get price from database with timestamp
    def get_price(self, time):
        if self.conn is None:
            return None
        c = self.conn.cursor()
        c.execute("SELECT price FROM prices WHERE time=?", (time,))
        price = c.fetchone()
        return price[0]

    # get latest available price from database
    def get_latest_available(self):
        return self.get_last_items(1)[0]

    # get latest n number of prices
    def get_last_items(self, items_nums):
        if self.conn is None:
            return None
        c = self.conn.cursor()
        c.execute(
            "SELECT price FROM prices ORDER BY time DESC LIMIT ?", (items_nums,))
        prices = c.fetchall()
        ret_val = []
        for price in prices:
            ret_val.append(price[0])
        return ret_val

    def close(self):
        self.conn.close()
