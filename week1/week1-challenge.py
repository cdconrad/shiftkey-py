# Week 1 Challenge: build a Tweet Retriever

# Can you create a script that takes a twitter screen_name and returns their
# most recent tweets? You can read more about the Twitter api at https://dev.twitter.com/rest/public

import tweepy
import time

# Twitter API credentials, as before. Get yours from apps.twitter.com.
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# this is used to collect the twitter names
from collections import defaultdict

# this function collects a twitter profile screen_name and returns their tweets
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        # Your code goes here! Hint: it will likely involve an array.
    except:
        # Your code goes here!

    return user_profile

# show that you can print the tweets
