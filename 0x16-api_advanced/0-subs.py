#!/usr/bin/python3

import praw

reddit = praw.Reddit(
    client_id='Fqw0sJNuqMWRB8LLVr-Cqg',
    client_secret='YzGW257awWZBnMB5wsagXvpOPT7HLg',
    user_agent='hbtn_red_api'
)


def number_of_subscribers(subreddit):
    """queries a subreddit and returns the number
    of subscribers"""
    if not reddit.subreddits.search_by_name(subreddit):
        return 0
    subs = reddit.subreddit(subreddit).subscribers
    return subs
