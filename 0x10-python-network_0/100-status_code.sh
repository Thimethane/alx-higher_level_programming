#!/bin/bash
# Use curl in a subshell and extract the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
