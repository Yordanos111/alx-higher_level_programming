#!/usr/bin/python3
def common_elements(set_1, set_2):
    list1_as_set = set(set_1)
    intersection = list1_as_set.intersection(set_2)
    common_element = list(intersection)
    return common_element
