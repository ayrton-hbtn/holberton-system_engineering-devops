#!/usr/bin/python3
"""100-count"""
import requests as req


def count_words(subreddit, word_list, after='', word_count={}):
    """parses the title of all hot articles and prints
    a sorted count of given keywords"""
    res = req.get('https://reddit.com/r/{}/hot/.json?limit=100\
                  &after={}'.format(subreddit, after),
                  headers={'User-Agent': 'Pepocho'}).json()
    try:
        after = res['data']['after']
    except KeyError:
        return
    for post in res['data']['children']:
        title = post['data']['title'].lower().split(' ')
        for word in word_list:
            for title_word in title:
                if word.lower() in title_word:
                    if word.lower() in word_count.keys():
                        word_count[word.lower()] += 1
                    else:
                        word_count[word.lower()] = 1
    if not after:
        word_list.sort()
        for word in set(word_list):
            if word in word_count.keys():
                print('{}: {}'.format(word, word_count[word]))
        return
    return count_words(subreddit, word_list, after, word_count)
