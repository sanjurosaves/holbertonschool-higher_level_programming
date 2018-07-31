#!/usr/bin/python3

def find_peak(list_of_integers):
    l = list_of_integers
    if not l:
        return None
    elif l[0] >= l[1]:
        return l[0]
    elif l[-1] >= l[-2]:
        return l[-1]
    else:
        i = (len(l) - 1)
        while i > 0:
            if l[i] >= l[i - 1]:
                return l[i]
            i = i - 1
