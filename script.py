import tweepy
from textblob import TextBlob

# Authentication Procedures
consumer_key= 'pPv5SdICAnWv29IWQEFw4Yqfs'
consumer_secret= 'FiNNV3yjp3hNl6z5x7CUib9XsIjujQiTVUCqNrTFkzFAHGvSGr'

access_token='879281158244126720-62EGb5s92KLmBHBO6LspP7pPMZ37jOC'
access_token_secret='i79u3X9QuZEsNKUc6FuXFHCm98O2KT798DsgBRVKQcneO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieving the tweets

query = raw_input()
public_tweets = api.search(query)


#Using iteration to access each tweet
for tweet in public_tweets:
    print(tweet.text)
    #perform sentiment analysis on the tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
