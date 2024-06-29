#!/usr/bin/python3
'''
    queries the Reddit API and prints the titles of the first 10 hot post
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        prints the titles of the first 10 hot posts listed for a given subreddit.
    '''
    headers = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=headers).json()
    try:
        for p in url.get('data').get('children'):
            print(p.get('data').get('title'))
    except Exception:
        print("None")


if __name__ == "__main__":
    top_ten(argv[1])