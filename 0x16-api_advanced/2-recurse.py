#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all hot articles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])
    for post in posts:
        hot_list.append(post.get('data', {}).get('title', None))

    after = data.get('after', None)
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
