#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
It also handles HTTP errors and displays the error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
