#!/usr/bin/python3
"""Queries the Reddit API."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom-agent'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print("None")
        for post in posts:
            print(post.get('data', {}).get('title', "None"))
    except (requests.RequestException, ValueError):
        print("None")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
