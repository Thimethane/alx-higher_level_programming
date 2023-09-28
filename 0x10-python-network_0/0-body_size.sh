#!/bin/bash
# Use curl to fetch the URL and pipe the response body to wc to count bytes
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

curl -s "$URL" | wc -c
