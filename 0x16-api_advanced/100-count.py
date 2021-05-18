#!/usr/bin/python3
""" Api advanced project """
import requests


def count_words(subreddit, word_list, after=None, count=0, sum_word={}):
    """parses the title of all hot articles, and prints a sorted count of given keywords"""
    if sum_word == {}:
        for word in word_list:
            sum_word[word] = 0
    res = requests.get(
        'https://www.reddit.com/r/{}/hot.json?after={}&count={})'
        .format(subreddit, after, count),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if res.status_code >= 300:
        return None
    for post in res.json().get('data').get('children'):
        title = post.get('data').get('title')
        for word in word_list:
            if word in title:
                sum_word[word] += 1
    after = res.json().get('data').get('after')
    count = res.json().get('data').get('count')
    if not after:
        sortedDict = dict( sorted(sum_word.items(), key=lambda x: x[0].lower()) )
        for key, value in sortedDict.items():
            if value != 0:
                print('{}: {}'.format(key, value))
        return
    return count_words(subreddit, word_list, after, count, sum_word)
