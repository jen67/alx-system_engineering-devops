#!/usr/bin/python3
import requests

def count_words(subreddit, word_list):
    """
    Queries the Reddit API and counts the occurrences of keywords in the hot posts of a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit to search.
    word_list (list): A list of words to search for in the hot posts' titles.
    
    Returns:
    None: If no posts or invalid subreddit, it returns nothing.
    """
    # Convert word_list to lowercase for case-insensitive comparison
    word_list = [word.lower() for word in word_list]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None  # Invalid subreddit

    posts = response.json().get('data', {}).get('children', [])
    
    word_count = {word: 0 for word in word_list}

    # Recursively count words
    def recurse(posts, after=None):
        nonlocal word_count
        
        # Iterate through posts
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_list:
                word_count[word] += title.split().count(word)
        
        # Check for more posts
        after = response.json().get('data', {}).get('after', None)
        if after:
            url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
            response = requests.get(url, headers=headers, allow_redirects=False)
            if response.status_code == 200:
                posts = response.json().get('data', {}).get('children', [])
                recurse(posts, after)

    recurse(posts)

    # Sort and print word counts
    word_count = {k: v for k, v in word_count.items() if v > 0}
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    if sorted_words:
        for word, count in sorted_words:
            print(f"{word}: {count}")

