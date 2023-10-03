#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
and displays the body of the response in a specific format.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("    - type:", type(response.text))
    print("    - content:", response.text)
