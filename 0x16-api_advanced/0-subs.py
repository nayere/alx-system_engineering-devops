#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    # Define the URL for the API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Define a custom User-Agent header
    headers = {
        'User-Agent': 'MyRedditApp/0.1 by MyRedditUser'  # You can use a descriptive identifier
    }
    
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers from the JSON data
        return data['data']['subscribers']
    else:
        # If the request was not successful, return 0
        return 0

if __name__ == '__main__':
    import sys
    
    # Testing the function
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"{subscribers}")
