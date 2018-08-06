#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests

    ag = sys.argv[1]
    url = 'https://swapi.co/api/people/?search='+ag

    r = requests.get(url)

    jso = r.json()
    print("Number of results: {}".format(jso['count']))
    for obj in jso['results']:
        print(obj['name'])
