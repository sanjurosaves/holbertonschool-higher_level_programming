#!/usr/bin/python3

if __name__ == '__main__':
    import urllib.request as ur
    import urllib.error
    import sys

    url = sys.argv[1]

    try:
        with ur.urlopen(url) as response:
            page = response.read()
            print(page.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
