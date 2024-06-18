#!/usr/bin/python3
"""Queries the Reddit API."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    data = response.json().get('data', {}).get('children', [])
    if not data:
        print("None")
        return
    for post in data:
        print(post.get('data', {}).get('title', "None"))
