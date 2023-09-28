#!/bin/bash
# Send a GET request with the specified header and display the response body
curl -sH "X-School-User-Id: 98" "$1"
