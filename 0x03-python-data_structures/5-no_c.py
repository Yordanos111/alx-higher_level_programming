#!/usr/bin/python3
def no_c(my_string):
    noc_string = ""
    for c in my_string:
        if not(c == 'c' or c == 'C'):
            noc_string += c
    return noc_string
