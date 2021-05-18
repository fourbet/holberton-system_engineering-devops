#!/usr/bin/python3
""" Api advanced project """
import requests


def count_words(subreddit, word_list, after=None, count=0, sum_word={}):
    """parses the title of all hot articles, and prints a sorted count of given keywords"""
    if sum_word == {}:
        for word in word_list:
            sum_word[word.lower()] = 0
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
            if word.lower() in title.lower():
                sum_word[word.lower()] += 1
    after = res.json().get('data').get('after')
    count = res.json().get('data').get('count')
    if not after:
        for key in sorted(sum_word.keys()):
            if sum_word[key] != 0:
                print('{}: {}'.format(key, sum_word[key]))
        return
    return count_words(subreddit, word_list, after, count, sum_word)
