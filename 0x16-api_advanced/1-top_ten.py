#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = 'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'ALXtask/0.0.1'}
    params = {'limit': 10}
    request = requests.get(url, allow_redirects=False, headers=headers,
                           params=params)
    if request.status_code == 200:
        for post in request.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
