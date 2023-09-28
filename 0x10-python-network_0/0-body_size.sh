#!/bin/bash
# Use curl to fetch the URL and pipe the response body to wc to count bytes
curl -s "$1" | wc -c
