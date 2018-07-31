#!/usr/bin/python3


def find_peak(list_of_integers):
    l = list_of_integers
    m = int(len(l) / 2)

    # print(m)

    if not l:
        return None
    elif (l[m] >= l[m-1]) or (l[m] >= l[m+1]):
        return l[m]
    elif l[m] < l[m-1]:
        # iterate through left half of list
        i = m - 1
        while i > 0:
            if l[i] >= l[i - 1]:
                return l[i]
            i = i - 1
    elif l[m] < l[m+1]:
        # iterate through right half of list
        i = m + 1
        while i < len(l):
            if l[i] >= l[i + 1]:
                return l[i]
            i = i + 1
