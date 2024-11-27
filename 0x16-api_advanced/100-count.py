#!/usr/bin/python3
import requests
import re

def count_words(subreddit, word_list, word_count={}):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'python3:count_keywords:v1.0 (by /u/your_username)'}
    
    response = requests.get(url, headers=headers, params={'after': word_count.get('after', None)}, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        
        for word in word_list:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + len(re.findall(r'\b' + re.escape(word) + r'\b', title))
    
    after = data['data'].get('after')
    if after:
        word_count['after'] = after
        count_words(subreddit, word_list, word_count)
    
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_words:
        if word != 'after' and count > 0:
            print(f'{word}: {count}')

