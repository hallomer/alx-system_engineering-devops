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


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
