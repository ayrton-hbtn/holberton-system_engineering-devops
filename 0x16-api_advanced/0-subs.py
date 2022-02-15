#!/usr/bin/python3

import requests as req


def number_of_subscribers(subreddit):
    """queries a subreddit and returns the number
    of subscribers"""
    res = req.get(f'https://reddit.com/r/{subreddit}.json',
                  headers={'User-Agent': 'Pepocho'}).json()
    try:
        return (res['data']['children'][0]['data']['subreddit_subscribers'])
    except KeyError:
        return 0
