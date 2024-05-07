#!/usr/bin/python3
""" A script for top 10 hot posts in a subreddit """
import requests


def top_ten(subreddit):
    """ returns the top 10 hot posts in  a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-agent': 'Bot/0.1'}

    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            all_data = response.json()
            if "data" in all_data and "children" in all_data['data']:
                for post in all_data['data']['children']:
                    print(post['data']['title'])
        else:
            return None
    except Exception as e:
        print(e)
