#!/usr/bin/python3
"""Queries the Reddit API."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:subreddit.top.ten:v1.0 (by /u/halomer)"}
    params = {'limit': 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    data = response.json().get("data", {}).get("children", [])
    for post in data:
        print(post.get("data", {}).get("title"))
