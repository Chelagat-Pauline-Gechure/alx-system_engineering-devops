#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given keywords
"""

import requests


def recurse(subreddit, hot_list=[], after=None, max_pages=None):
    """
    returning top ten post titles recursively
    """
    if max_pages is not None and max_pages <= 0:
        return hot_list

    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after} if after else {}

    request = requests.get(
        base_url,
        params=params,
        headers={'User-Agent': 'Chelagat Pauline Gechure'},
        allow_redirects=False
    )

    if request.status_code != 200:
        return None  
    data = request.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    next_page = data.get('data', {}).get('after')
    if next_page:
        return recurse(
            subreddit, hot_list, after=next_page, max_pages=max_pages
        )

    return hot_list if len(hot_list) > 0 else None
