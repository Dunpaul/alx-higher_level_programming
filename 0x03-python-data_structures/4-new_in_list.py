#!/bin/python3

def new_in_list(my_list, idx, element):
    list_n = my_list.copy()
    if idx < 0 or idx > len(list_n) - 1:
        return list_n
    if list_n[idx]:
        list_n[idx] = element
    return list_n
