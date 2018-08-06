#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    try:
        r = requests.get(url)
        if r.status_code == '404':
            print("Error code: 404")
        else:
            print(r.text)
    except HTTPError:
        print("Error code: {}".format(r.raise_for_status()))
