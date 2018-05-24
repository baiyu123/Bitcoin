import unittest
import sys
sys.path.append('/Users/baiyuhuang/Desktop/Bitcoin')
from database import PriceDatabase
# python -m unittest test_database.TestDatabase


class TestDatabase(unittest.TestCase):

    def test_add_price(self):
        db = PriceDatabase()
        db.connect_database(':memory:')
        db.create_price_table()
        db.save_price(1234, 1000.0)
        price = db.get_price(1234)
        self.assertEqual(price, 1000.0)

    def test_get_first_5(self):
        db = PriceDatabase()
        db.connect_database(':memory:')
        db.create_price_table()
        db.save_price(1, 1000.0)
        db.save_price(2, 2000.0)
        db.save_price(3, 3000.0)
        db.save_price(4, 4000.0)
        db.save_price(5, 5000.0)
        db.save_price(6, 6000.0)
        price = db.get_last_items(5)
        self.assertEqual(price[0], 6000.0)
        self.assertEqual(price[1], 5000.0)
        self.assertEqual(price[2], 4000.0)
        self.assertEqual(price[3], 3000.0)
        self.assertEqual(price[4], 2000.0)

    def test_get_latest(self):
        db = PriceDatabase()
        db.connect_database(':memory:')
        db.create_price_table()
        db.save_price(1, 1000.0)
        db.save_price(2, 2000.0)
        db.save_price(3, 3000.0)
        db.save_price(4, 4000.0)
        db.save_price(5, 5000.0)
        db.save_price(6, 6000.0)
        price = db.get_latest_available()
        self.assertEqual(price, 6000.0)

if __name__ == '__main__':
    unittest.main()
