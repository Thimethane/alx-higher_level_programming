#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Use curl to fetch the URL and pipe the response body to wc to count bytes
curl -s "$URL" | wc -c
