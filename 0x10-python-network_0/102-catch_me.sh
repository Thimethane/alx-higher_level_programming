#!/bin/bash
# Send a PUT request with a custom header to cause the server to respond with the desired message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
