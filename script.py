import tweepy
from textblob import TextBlob
import json
from pprint import pprint

json_file = './keys.sec'
keyword = "Microsoft"


secrets = json.load(open(json_file))

consumer_key = secrets['consumer_key']
consumer_secret = secrets['consumer_secret']

access_token = secrets['access_token']
access_token_secret = secrets['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search(keyword)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    # polarity measure positive or negative
    # subjectivity opinion or factual