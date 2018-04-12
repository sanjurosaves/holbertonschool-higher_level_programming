#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) is 1:
        print('{} arguments.'.format((len(sys.argv) - 1)))
    elif len(sys.argv) is 2:
        print('{} argument:'.format((len(sys.argv) - 1)))
    else:
        print('{} arguments:'.format((len(sys.argv) - 1)))

    argc = 1
    while argc < len(sys.argv):
        print('{}: {}'.format(argc, sys.argv[argc]))
        argc += 1
