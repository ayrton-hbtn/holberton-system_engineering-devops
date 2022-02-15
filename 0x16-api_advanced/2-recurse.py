#!/usr/bin/python3

import requests as req


def recurse(subreddit, hot_list=[], after=''):
    """returns a list containing the titles of all
    hot articles for a given subreddit, recursively"""
    res = req.get(f'https://reddit.com/r/{subreddit}/hot/.json?limit=100\
                  &after={after}',
                  headers={'User-Agent': 'Pepocho'}).json()
    try:
        after = res['data']['after']
    except KeyError:
        return None
    for post in res['data']['children']:
        hot_list.append(post['data']['title'])
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
