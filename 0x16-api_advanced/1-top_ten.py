#!/usr/bin/python3
"""
Module Docs
"""
import requests


def top_ten(subreddit):
    """
    Function Docs
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Google Chrome 124.0.6367.119 (Official Build) (64-bit)'
    }
    response = requests.get('{}/r/{}/.json?sort={}&limit={}'.format(
        url, subreddit, 'top', 10),
        headers=header,
        allow_redirects=False)
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
