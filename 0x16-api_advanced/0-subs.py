#!/usr/bin/python3
""" A script to return the total number of subscribers in a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers in a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Bot/0.1'}

    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            all_data = response.json()
            #print(all_data)
            if "data" in all_data and "subscribers" in all_data['data']:
                subscribers = all_data['data']['subscribers']
                return subscribers
        else:
            return 0
    except Exception as e:
        print(e)
