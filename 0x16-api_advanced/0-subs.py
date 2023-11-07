#!/usr/bin/python3
"""
subreddit subscriber numbers
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that querrying Reddit API then  returning subscriber numbers
    for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    agent_user = {'User-agent': 'Chelagat Pauline Gechure'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=agent_user)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
