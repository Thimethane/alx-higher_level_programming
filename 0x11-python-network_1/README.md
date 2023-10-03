0x11. Python - Network #1


This repository contains solutions and explanations for the "0x11. Python - Network #1" project tasks. In this project, we explore working with network requests in Python, using libraries like urllib and requests to interact with web resources, fetch JSON data, and manipulate external services.

Task 1: Fetching Internet Resources with urllib
File: 0-hbtn_status.py

This script fetches an internet resource (specifically, https://alx-intranet.hbtn.io/status) using the urllib package in Python. It displays information about the body of the response, including its type and content.

Usage:

bash
Copy code
./0-hbtn_status.py


Task 2: Displaying Response Header with requests
File: 1-hbtn_header.py

This script uses the requests package to send an HTTP request to a given URL and displays the value of the X-Request-Id variable found in the header of the response.

Usage:

bash
Copy code
./1-hbtn_header.py <URL>

Task 3: Fetching a URL with Parameters
File: 2-post_email.py

This script takes a URL and an email as command-line arguments, sends a POST request to the URL with the email as a parameter, and displays the body of the response.

Usage:

bash
Copy code
./2-post_email.py <URL> <email>

Task 4: Handling HTTP Errors
File: 3-error_code.py

This script sends a request to a URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message with the status code.

Usage:

bash
Copy code
./3-error_code.py <URL>

Task 5: Fetching Data with a Parameter
File: 4-hbtn_status.py

This script fetches an internet resource (https://alx-intranet.hbtn.io/status) using the requests package and displays information about the body of the response.

Usage:

bash
Copy code
./4-hbtn_status.py

Task 6: Fetching Data with a Parameter
File: 5-hbtn_header.py

This script uses the requests package to send an HTTP request to a URL and displays the value of the X-Request-Id variable found in the header of the response.

Usage:

bash
Copy code
./5-hbtn_header.py <URL>

Task 7: Fetching Data with a Parameter
File: 6-post_email.py

This script takes a URL and an email as command-line arguments, sends a POST request to the URL with the email as a parameter, and displays the body of the response.

Usage:

bash
Copy code
./6-post_email.py <URL> <email>

Task 8: Fetching Data with a Parameter
File: 7-error_code.py

This script sends a request to a URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message with the status code.

Usage:

bash
Copy code

./7-error_code.py <URL>
Task 9: Fetching Data with a Parameter
File: 8-json_api.py

This script sends a POST request with a letter as a parameter and displays the ID and name from the JSON response. If the JSON is invalid or empty, appropriate error messages are displayed.

Usage:

bash
Copy code
./8-json_api.py <letter>

Task 10: Fetching Data with a Parameter
File: 10-my_github.py

This script takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user's ID. It uses Basic Authentication with a personal access token as the password.

Usage:

bash
Copy code
./10-my_github.py <github_username> <personal_access_token>
