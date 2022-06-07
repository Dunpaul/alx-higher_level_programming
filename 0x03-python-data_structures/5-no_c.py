#!/usr/bin/python3

def no_c(my_string):
    str_ls = list(my_string)
    for chr in str_ls:
        if chr == 'c' or chr == 'C':
            str_ls.remove(chr)
    newSt = ''.join(str_ls)
    return(newSt)
