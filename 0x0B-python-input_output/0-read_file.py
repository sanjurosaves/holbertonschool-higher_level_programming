#!/usr/bin/python3

def read_file(filename=""):
    with open('my_file_0.txt', encoding ='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
