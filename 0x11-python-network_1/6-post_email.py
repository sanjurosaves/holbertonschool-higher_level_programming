#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    eml = sys.argv[2]

    payload = {'email': eml}

    r = requests.post(url, data=payload)

    print(r.text)
