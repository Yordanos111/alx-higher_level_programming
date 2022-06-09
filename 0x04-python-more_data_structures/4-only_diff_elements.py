#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list3 = set_1 ^ set_2
    list4 = list(list3)
    return list4
