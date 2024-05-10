#!/usr/bin/python3
"""
Module Docs
"""
import requests


def count_words(subreddit, word_list, instances={}, after=""):
    """
    Function Docs
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Google Chrome 124.0.6367.119 (Official Build) (64-bit)'
    }
    if not instances:
        for word in word_list:
            if word.lower() not in instances:
                instances[word.lower()] = 0

    if after is None:
        instances = sorted(
                instances.items(),
                key=lambda key_value: (-key_value[1], key_value[0])
                )
        for key, value in instances.items():
            print("{}: {}".format(key, value))
        return None

    response = requests.get(
            '{}/r/{}/hot/.json?limit={}&after={}'.format(
                url, subreddit, 100, after),
            headers=header,
            allow_redirects=False)
    try:
        if response.status_code != 200:
            raise Exception
    except Exception:
        return None

    try:
        hot = response.json()['data']['children']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]
            for word in instances.keys():
                instances[word] += lower.count(word)

    except Exception:
        return None
    count_words(subreddit, word_list, instances, after)
