import tweepy
from textblob import TextBlob
from secret import *

'''consumer_key
consumer_secret 

access_token 
access_secret'''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

tweet_bucket = api.search('Tom Brady')

for tweet in tweet_bucket:
	print tweet.text 
	analysis = TextBlob(tweet.text)
	print analysis.sentiment 
	print '\n\n'

	
'''
piece = TextBlob("Tom Brady is the greatest quarterback in NFL history!")


print piece.tags 

print piece.words 


#-1 to 1 scale for polarity 
print piece.sentiment.polarity'''