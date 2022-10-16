#!/usr/bin/python3
from sys import argv
from math import floor
"""A Program to factorize as many numbers as
possible into a product of two smaller numbers."""

if len(argv) != 2:
    exit()

file_name = argv[1]

def factorize(num):
    """factorize a given number into 2 factors"""
    if num < 2:
        return
    for fac in range (2, (floor(num ** 0.5) + 1)):
            if num % fac == 0:
                print("{:.0f}={:.0f}*{:.0f}".format(num, num // fac, fac))
                return

try:
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break

            num = int(line.split('\n')[0])
            factorize(num)
except:
    pass

