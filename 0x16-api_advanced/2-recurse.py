#!/usr/bin/python3
""" A script for recursively finding the  top 10 hot posts in a subreddit """
import requests


def recurse(subreddit, hot_list[]=None, after=None):
    """ returns the top 10 hot posts in  a subreddit """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-agent': 'Bot/0.1'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)
    try:
        if response.status_code == 200:
            all_data = response.json()
            if "data" in all_data and "children" in all_data['data']:
                for post in all_data['data']['children']:
                    hot_list.append(post['data']['title'])

                    if all_data['data']['after']:
                        recurse(subreddit, hot_list, data['data']['after'])
                    else:
                        return hot_list
        else:
            return None
    except Exception as e:
        print(e)
