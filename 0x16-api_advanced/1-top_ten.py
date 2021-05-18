#!/usr/bin/python3
""" Api advanced project """
import requests


def top_ten(subreddit):
    """queries the Reddit API and
    prints the titles of the first 10 hot posts"""
    res = requests.get('https://www.reddit.com/r/{}/top.json?limit=10'
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False,
                       )
    print(res.status_code)
    if res.status_code >= 300:
        print(None)
    for post in res.json().get('data').get('children'):
        print(post.get('data').get('title'))
