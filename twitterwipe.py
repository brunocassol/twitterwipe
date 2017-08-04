#!/usr/bin/env python
# encoding: utf-8
"""
Deletes all tweets, retweets and favorites.

Installation:

1/ pip install python-twitter
2/ go to https://apps.twitter.com, sign up with your account and create a new app (the details can be bogus, your app will be private)
3/ make sure the app has read, write permission and CLICK "Regenerate My Access Token and Token Secret" button (IMPORTANT)
4/ copy consumer_key, consumer_secret, access_token_key and access_token_secret from your app to the placeholders below
5/ run this with python 2: python twitterwipe.py

Based on: https://github.com/olivierthereaux/oldtweets/blob/master/oldtweets.py
"""

import time
import twitter
import sys

def main(argv=None):

    api = twitter.Api(
        consumer_key='INSERT_HERE',
        consumer_secret='INSERT_HERE',
        access_token_key='INSERT_HERE',
        access_token_secret='INSERT_HERE')

    REMOVE_TWEETS_AND_RETWEETS = True
    REMOVE_FAVORITES = True

    while REMOVE_TWEETS_AND_RETWEETS:
        tweets = api.GetUserTimeline(count=200, include_rts=True)
        if len(tweets) == 0:
            print("\nNo remaining tweets found... Wiping favorites next.")
            break
        for tweet in tweets:
            print("\nDeleting tweet id: ", tweet.id)
            try:
                status = api.DestroyStatus(tweet.id)
                print(status)
                time.sleep(2)
            except Exception as e:
                pass
                time.sleep(1)

    while REMOVE_FAVORITES:
        favorites = api.GetFavorites(count=200)
        if len(favorites) == 0:
            print("\nNo remaining favorites found... Exiting.")
            break
        for favorite in favorites:
            print("\nRemoving favorite from tweet id: ", favorite.id)
            try:
                status = api.DestroyFavorite(status_id=favorite.id)
                print(status)
                time.sleep(1)
            except Exception as e:
                pass
                time.sleep(1)

if __name__ == "__main__":
    sys.exit(main())