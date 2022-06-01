#!/usr/bin/python3


def fizzbuzz():
    for fizbuz in range(1, 101):
        if fizbuz % 15 == 0:
            print("FizzBuzz ", end='')
        elif fizbuz % 3 == 0:
            print("Fizz ", end='')
        elif fizbuz % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(fizbuz), end='')
