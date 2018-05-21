import urllib2
import json


class BitcoinPrice:
    site = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    def __init__(self):
        pass

    def get_current_price(self):
        req = urllib2.Request(self.site, headers=self.hdr)
        response = urllib2.urlopen(req).read()
        response_dict = json.loads(response)
        current_price = response_dict['bpi']['USD']['rate']
        return current_price
