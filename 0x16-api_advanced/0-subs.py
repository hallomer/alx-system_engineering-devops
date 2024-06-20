#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers."""
    if not subreddit:
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
