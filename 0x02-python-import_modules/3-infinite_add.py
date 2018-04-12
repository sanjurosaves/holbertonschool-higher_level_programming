#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    argc = 1
    while argc < len(sys.argv):
        sum += int(sys.argv[argc])
        argc += 1
    print(sum)
