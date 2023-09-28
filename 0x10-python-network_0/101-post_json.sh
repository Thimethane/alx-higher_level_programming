#!/bin/bash
# Send a POST request with the JSON file as the request body and display the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
