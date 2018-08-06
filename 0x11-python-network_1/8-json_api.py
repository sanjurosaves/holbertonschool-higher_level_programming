#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    let = sys.argv[2]

    if let is None:
        payload = {'q': ""}
    else:
        payload = {'q': let}

    r = requests.post(url, data=payload)

    print(r.json)
