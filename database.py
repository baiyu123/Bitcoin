import sqlite3


class PriceDatabase:
    conn = None
    database = ''

    def __init__(self):
        pass

    def connect_database(self, database):
        self.conn = sqlite3.connect(database)
        self.database = database

    def create_price_table(self):
        if self.conn is None:
            return
        with self.conn:
            c = self.conn.cursor()
            c.execute("""CREATE TABLE prices(time INTEGER, price REAL)""")

    def save_price(self, time, price):
        if self.conn is None:
            return
        with self.conn:
            c = self.conn.cursor()
            c.execute("INSERT INTO prices VALUES (?, ?)",
                      (time, price))

    def get_price(self, time):
        if self.conn is None:
            return None
        c = self.conn.cursor()
        c.execute("SELECT price FROM prices WHERE time=?", (time,))
        price = c.fetchone()
        return price[0]

    def close(self):
        self.conn.close()
