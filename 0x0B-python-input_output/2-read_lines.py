#!/usr/bin/python3

def read_lines(filename="", nb_lines=0):
    n = 0
    with open('my_file_0.txt', encoding ='utf-8') as a_file:
        for line in a_file:
            n += 1
        a_file.seek(0)
        if nb_lines <= 0 or nb_lines >= n:
            for line in a_file:
                print(line, end="")
        else:
            x = 0
            while x < nb_lines:
                print(a_file.readline(), end="")
                x += 1
