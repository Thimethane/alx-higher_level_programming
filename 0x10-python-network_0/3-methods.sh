#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send an OPTIONS request and display the allowed HTTP methods
curl -s -I -X OPTIONS "$URL" | grep "Allow:" | cut -d ' ' -f 2-
