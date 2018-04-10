#!/usr/bin/python3
for p in range(1, 90):
    if (p // 10 != p % 10) and ((((p % 10) * 10) + (p // 10)) > p) and p < 89:
        print('{:02d}, '.format(p), end='')
    if p > 88:
        print('{:02d}'.format(p))
