import tweepy
from quotes_script import forismatic_quote


auth = tweepy.OAuthHandler('Juhag2Ovsz8xHOl7kUAY7wo7w','6vJdWqWyuLb2IxuzoEfcCa6nsVa7FhLIkO1CgAFfygMAkLQvxA')
auth.set_access_token('928329690233782272-TBFkSJks1LrP5AbT2jwgmkxCxBfXQ2Y','x8BdymrkDvZaL3zZxJ73KoWmHOhx5nSvg9Ygv9elDtK7k')

api = tweepy.API(auth)

quote = forismatic_quote()
quote_text = quote.get_quote()
quote_author = quote.get_author()

tweet = '%s \n\nAuthor: %s \nTwitter Quote bot created by: EbonicsTooter' % (quote_text,quote_author)

print(api.update_status(tweet))