#!/usr/bin/python3
for p in range (1, 80):
    if (p // 10 is not p % 10) and ((((p % 10) * 10) + (p // 10)) > p):
        print('{:02d}, '.format(p), end='')
print('89')
