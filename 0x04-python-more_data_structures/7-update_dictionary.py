#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if value in a_dictionary:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
    else:
        a_dictionary[key] = value
    print(a_dictionary)
