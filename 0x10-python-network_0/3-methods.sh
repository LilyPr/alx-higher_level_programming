#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS $1 -i | grep Allow | awk -F ":" '{print $2}' | cut -d ' ' -f 2-
