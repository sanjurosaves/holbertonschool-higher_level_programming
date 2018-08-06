#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    try:
        let = sys.argv[1]
        payload = {'q': let}
    except:
        payload = {'q': ""}

    r = requests.post(url, data=payload)

    jso = r.json()
    try:
        print("[{}] {}".format(jso['id'], jso['name']))
    except:
        print("No result")
