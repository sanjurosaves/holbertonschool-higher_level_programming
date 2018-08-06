#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    u = sys.argv[1]
    p = sys.argv[2]
    url = 'https://api.github.com/users/'+u

    r = requests.get(url, auth=HTTPBasicAuth(u, p))

    jso = r.json()
    print(jso.get('id'))
