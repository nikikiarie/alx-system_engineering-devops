#!/usr/bin/python3
"""
Queries subscribers on  a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subs on subreddit"""
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
