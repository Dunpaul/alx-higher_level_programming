#!/usr/bin/python3
for ch in range(93, 127):
    if chr(ch) != 'e' and chr(ch) != 'q':
        print("{}".format(chr(ch)), end='')
