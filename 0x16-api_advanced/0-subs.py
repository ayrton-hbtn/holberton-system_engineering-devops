#!/usr/bin/python3
"""0-subs"""
import requests as req


def number_of_subscribers(subreddit):
    """queries a subreddit and returns the number
    of subscribers"""
    res = req.get('https://reddit.com/r/{}.json'.format(subreddit),
                  headers={'User-Agent': 'Pepocho'}).json()
    try:
        return (res['data']['children'][0]['data']['subreddit_subscribers'])
    except KeyError:
        return 0
