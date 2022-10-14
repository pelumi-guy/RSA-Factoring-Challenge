#!/usr/bin/python3
import sys
from math import floor
"""A Program to factorize as many numbers as
possible into a product of two smaller numbers."""

file_name = sys.argv[1]

with open(file_name) as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        num = int(line)
        for fac in range (2, (floor(num ** 0.5) + 1)):
            if num % fac == 0:
                break
        if fac == floor(num ** 0.5) and num % fac != 0:
            print("{}={}*{}".format(num, num, 1))
        else:
            fac2 = num // fac
            print("{}={}*{}".format(num, fac2, fac))
