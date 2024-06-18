#!/usr/bin/python3
"""Queries the Reddit API."""
import requests

def count_words(subreddit, word_list, hot_list=[], after=''):
    """Parses the title of all hot articles, and prints a sorted count."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])
    for post in posts:
        hot_list.append(post.get('data', {}).get('title', '').lower())

    after = data.get('after', None)
    if after:
        return count_words(subreddit, word_list, hot_list, after)

    word_count = {}
    for word in word_list:
        word_count[word.lower()] = 0

    for title in hot_list:
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] += title.split().count(word_lower)

    sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")
