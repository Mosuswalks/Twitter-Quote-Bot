import urllib3
import json


class forismatic_quote:

    def __init__(self):
        http = urllib3.PoolManager()
        self.forismatic = http.request('GET',
                                     'http://api.forismatic.com/api/1.0/',
                                      fields={'method':'getQuote','format':'json','lang':'en'})

    def get_quote(self):
        self.quote = json.loads(self.forismatic.data.decode('utf-8'))['quoteText']
        return self.quote

    def get_author(self):
        self.author = json.loads(self.forismatic.data.decode('utf-8'))['quoteAuthor']
        return self.author