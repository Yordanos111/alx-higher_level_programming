#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        for i in my_list:
            if my_list[i] == idx:
                my_list[i+1] = element
        return (my_list)
