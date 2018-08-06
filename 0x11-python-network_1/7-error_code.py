#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    try:
        r = requests.get(url)
        print(r.text)
    except HTTPError
        print("Error code: {}".format(r.raise_for_status()))
