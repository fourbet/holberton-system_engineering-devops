#!/usr/bin/python3
""" Api advanced project """
import requests


def top_ten(subreddit):
    """queries the Reddit API, prints the titles of the first 10 hot posts"""
    res = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False,
                       )
    if res.status_code >= 300:
        print(None)
        return
    for post in res.json().get('data').get('children'):
        print(post.get('data').get('title'))
