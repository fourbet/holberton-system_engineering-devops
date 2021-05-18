#!/usr/bin/python3
""" Api advanced project """
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """returns a list containing the titles of all hot articles"""
    res = requests.get(
        'https://www.reddit.com/r/{}/hot.json?after={}&count={})'
        .format(subreddit, after, count),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if res.status_code >= 300:
        return None
    for post in res.json().get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    after = res.json().get('data').get('after')
    count = res.json().get('data').get('count')
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after, count)
