#!/usr/bin/python3
for ch in range(93, 127):
    if ch != 101 and ch != 113:
        print("{}".format(chr(ch)), end="")
