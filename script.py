import sys, json, argparse

import tweepy
from textblob import TextBlob

JSON_FILE = './keys.sec'
CONSTANT_KEYWORD = "#Microsoft"

'''
    Go to https://apps.twitter.com/new/app
    Create tokens for your application and
    create a file called keys.sec in root directory.
    Copy paste keys, tokens and secrets into json
    e.g.
    {
        "consumer_key" : "CONUMSER_KEY",
        "consumer_secret" : "CONSUMER_SECRET",
        "access_token" : "ACCESS_TOKEN",
        "access_token_secret" : "ACCESS_TOKEN_SECRET"
    }

    @return tweepy api object
'''
def create_api(secret_json_file = JSON_FILE):
    secrets = json.load(open(secret_json_file))

    consumer_key = secrets['consumer_key']
    consumer_secret = secrets['consumer_secret']

    access_token = secrets['access_token']
    access_token_secret = secrets['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

'''
    Uses provided api to call search for given keyword
    Method enumerates tweet text
    Run analysis with TextBlob to get 
    polarity which measure positive or negative
    and subjectivity which opinion or factual
'''
def analysis_sentiment(api, keyword):
    public_tweets = api.search(keyword)
    i = 0
    print("Number\tPolarity\tSubjectivity\tTweet Text")
    for tweet in public_tweets:
        i += 1
        analysis = TextBlob(tweet.text)
        print("%i\t%f\t%f\t%s" % (i, analysis.sentiment.polarity, analysis.sentiment.subjectivity, tweet.text))


def main():
    keyword = CONSTANT_KEYWORD

    parser = argparse.ArgumentParser()
    parser.add_argument("-keyword", help="Use keyword to query twitter api")
    args = parser.parse_args()
    if (args.keyword):
        keyword = args.keyword

    print("Query twitter with keyword: %s" % (keyword))
    api = create_api()
    analysis_sentiment(api, keyword)

if __name__ == "__main__":
   main()
