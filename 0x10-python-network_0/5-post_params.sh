#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$URL"
