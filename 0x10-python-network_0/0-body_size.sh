#!/bin/bash
# displays the size of the body of the response to the URL request
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2
