#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-agent'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except Exception:
        return 0