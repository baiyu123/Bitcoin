import unittest
import sys
sys.path.append('/Users/baiyuhuang/Desktop/Bitcoin')
from database import PriceDatabase


class TestDatabase(unittest.TestCase):

    def test_add_price(self):
        db = PriceDatabase()
        db.connect_database(':memory:')
        db.create_price_table()
        db.save_price(1234, 1000.0)
        price = db.get_price(1234)
        self.assertEqual(price, 1000.0)


if __name__ == '__main__':
    unittest.main()
