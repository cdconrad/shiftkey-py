# Week 1 Challenge: build a Tweet Retriever

# Can you create a script that takes a twitter screen_name and returns their
# most recent tweets? You can read more about the Twitter api at https://dev.twitter.com/rest/public

import tweepy
import time

# Twitter API credentials, as before. Get yours from apps.twitter.com.
consumer_key = "cKqgI5UYfGRWUqKuf39Tvn86m"
consumer_secret = "PbtAMTs6VbMH4HU29mxNV88g0bQTSMHTcWwln2z0gNdAomTvIx"
access_key = "494233327-oBU1RXqfi4z9MEzktYHhA1c52b2xEMy56f1diuW4"
access_secret = "9RThiwYYL5twQa1MVc67pxUluGy0muW1vTI4OFgliRCl9"

# this is used to collect the twitter names
from collections import defaultdict

# this function collects a twitter profile screen_name and returns their tweets
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        tweets = api.user_timeline(screen_name = screen_name, count=1)
        for x in tweets:
            print x.text
    except:
        print "Not working"
    return tweets

tweets = get_profile("cd_conrad")

# show that you can print the tweets
