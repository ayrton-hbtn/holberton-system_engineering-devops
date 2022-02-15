#!/usr/bin/python3
"""1-top_ten"""
import requests as req


def top_ten(subreddit):
    """queries the titles of the first 10 hot posts
    listed for a given subreddit"""
    res = req.get(f'https://reddit.com/r/{subreddit}/top/.json?limit=10',
                  headers={'User-Agent': 'Pepocho'}).json()
    try:
        for post in res['data']['children']:
            print(post['data']['title'])
    except KeyError:
        print('None')
