from sys import argv
from math import floor

if len(argv) != 2:
    exit()


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
    if num < 2:
        return

    x = num
    if num < MAXN: #intelligent factorisation using Sieve of Eratosthenes
        while (x != 1 and x < (floor(num ** 0.5) + 1)):
            x = x // spf[x]
            if isPrime(num/x):
                return x
        return None
    else: #brute factorisation
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
        return None


file_name = argv[1]

try:
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break

            num = int(line)
            fac = getFactorization(num)
            print("{:.0f}={:.0f}*{:.0f}".format(num, num//fac, fac))
except:
    pass