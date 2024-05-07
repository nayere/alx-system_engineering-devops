#!/bin/bash

# Function to get the number of subscribers for a given subreddit
number_of_subscribers() {
    # Define the subreddit passed as argument
    local subreddit="$1"
    
    # Define the URL for the API endpoint
    local url="https://www.reddit.com/r/${subreddit}/about.json"
    
    # Set a custom User-Agent header
    local user_agent="MyRedditApp/0.1 by MyRedditUser"
    
    # Send a GET request to the URL using curl
    response=$(curl -s -A "$user_agent" "$url")

    # Check if the request was successful by checking the HTTP status code
    http_status=$(echo "$response" | jq -r '.message')

    # If the request was successful (http_status is null or empty)
    if [ "$http_status" = "Not Found" ]; then
        # The subreddit is invalid, return 0
        echo 0
    else
        # Extract the number of subscribers from the JSON response using jq
        subscribers=$(echo "$response" | jq -r '.data.subscribers')

        # Return the number of subscribers
        echo "$subscribers"
    fi
}

# Main script execution
if [ "$#" -lt 1 ]; then
    echo "Please pass an argument for the subreddit to search."
else
    # Call the function and print the number of subscribers
    subreddit="$1"
    subscribers=$(number_of_subscribers "$subreddit")
    echo "$subscribers"
fi
