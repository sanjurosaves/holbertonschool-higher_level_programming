#!/usr/bin/python3
import urllib.request
import sys
"""
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""


url = sys.argv[1]
data = None
headers = {'User-Agent': 'Python-urllib/3.4'}
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
    page = response.info()
print(page['X-Request-Id'])
