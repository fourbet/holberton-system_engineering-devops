#!/usr/bin/python3
""" Api advanced project """
import requests


def number_of_subscribers(subreddit):
    """ queries Reddit API and returns number of subscribers """
    res = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if res.status_code >= 300:
        return 0
    subs = res.json().get('data').get('subscribers')
    return subs
