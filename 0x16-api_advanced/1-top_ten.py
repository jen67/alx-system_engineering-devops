#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python3:top_ten_posts:v1.0 (by /u/your_username)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    for post in data['data']['children']:
        print(post['data']['title'])

