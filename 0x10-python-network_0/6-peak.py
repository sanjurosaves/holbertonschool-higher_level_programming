#!/usr/bin/python3


def find_peak(list_of_integers):
    l = list_of_integers
    m = len(l) // 2
    print("mid is {}".format(m))

    if not l:
        return None
    elif (l[m] >= l[m-1]) and (l[m] >= l[m+1]):
        return l[m]
    elif (m > 0) and (l[m] <= l[m-1]):
        # iterate through left half of list
        i = m - 1
        while i > 0:
            if l[i] >= l[i - 1]:
                return l[i]
            i = i - 1
    else: #if l[m] < l[m+1]:
        # iterate through right half of list
        i = m + 1
        while i < len(l):
            if l[i] >= l[i + 1]:
                return l[i]
            i = i + 1
