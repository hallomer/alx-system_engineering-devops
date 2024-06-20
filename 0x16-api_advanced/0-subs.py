#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'ALXtask/0.0.1'}
    request = requests.get(url, allow_redirects=False, headers=headers)
    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    return 0
