import tweepy
from quotes_script import forismatic_quote


auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)

quote = forismatic_quote()
quote_text = quote.get_quote()
quote_author = quote.get_author()

tweet = '%s \n\nAuthor: %s \nTwitter Quote bot created by: Replace_With_Your_Handle' % (quote_text,quote_author)

print(api.update_status(tweet))
