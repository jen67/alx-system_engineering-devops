#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'python3:recurse_hot_posts:v1.0 (by /u/your_username)'}
    
    response = requests.get(url, headers=headers, params={'after': hot_list[-1] if hot_list else None}, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])
    
    after = data['data'].get('after')
    if after:
        return recurse(subreddit, hot_list)
    
    return hot_list

