#!/usr/bin/env python
# encoding: utf-8

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