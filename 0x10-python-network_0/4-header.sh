#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send a GET request with the specified header and display the response body
curl -s -H "X-School-User-Id: 98" "$URL"
