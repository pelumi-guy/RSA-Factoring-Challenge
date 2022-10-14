import sys
from smallest_prime_factors import spf
from math import floor

MAXN = 1000001


def isPrime(num):
    """Function to determine if a number is a prime number or not

    Return:
        True: If number is prime
        False: If number is composite
    """
    if num < MAXN:
        if spf[num] == num:
            return True
        else:
            return False
    else:
        for i in range(2, floor(num ** 0.5)):
            if num % i == 0:
                return False
        return True

def getFactorization(num):
    """Function to factorize a number into prime factors

    Return:
        smallest prime factor that has a prime quotient
    """
    x = num
    if num < MAXN:
        while (x != 1 and x < (floor(num ** 0.5) + 1)):
            x = x // spf[x]
            if isPrime(num/x):
                return x
        return 1
    else:
        for i in range(2, (floor(num ** 0.5) + 1)):
            j = i
            if num % i == 0:
                if isPrime(i):
                    if isPrime(num // i):
                        return i
                    elif i < MAXN:
                        while (j != 1 and j < (floor(num ** 0.5) + 1)):
                            j = j // spf[j]
                            if isPrime(num/j):
                                return j
        return 1


file_name = sys.argv[1]

with open(file_name) as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        num = int(line)
        fac = getFactorization(num)
        print("{}={}*{}".format(num, num//fac, fac))
