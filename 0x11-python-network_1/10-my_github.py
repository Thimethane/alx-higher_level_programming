#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token) and
uses the GitHub API to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API endpoint to get user information
    api_url = "https://api.github.com/user"

    # Set up authentication using Basic
    # Authentication with personal access token
    auth = (username, password)

    try:
        response = requests.get(api_url, auth=auth)
        if response.status_code == 200:
            # Print the user's ID
            print(response.json()['id'])
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("None")
