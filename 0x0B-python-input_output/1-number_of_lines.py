#!/usr/bin/python3

def number_of_lines(filename=""):
    number_of_lines = 0
    with open('my_file_0.txt', encoding ='utf-8') as a_file:
        for line in a_file:
            number_of_lines += 1
    return number_of_lines
