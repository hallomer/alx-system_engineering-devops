#!/usr/bin/python3
"""Queries the Reddit API."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers='Custom', params={"limit": "10"})

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
