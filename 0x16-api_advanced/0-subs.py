#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
    except Exception:
        return 0

    if data is None or 'subscribers' not in data:
        return 0

    return data.get('subscribers')
