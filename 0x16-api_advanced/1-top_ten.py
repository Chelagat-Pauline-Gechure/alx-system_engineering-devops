#!/usr/bin/python3

"""
prints titles of first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function querrying Reddit API & printing title of first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    agent_user = {'User-agent': 'Chelagtat Pauline Gechure'}
    parameters = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=agent_user, params=parameters)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
