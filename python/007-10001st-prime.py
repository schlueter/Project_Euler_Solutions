#!/usr/bin/env python

from sys import argv

from util.generators import prime_numbers


if __name__ == "__main__":
    target = int(argv[1])
    primes = prime_numbers()
    for i in xrange(target - 1): primes.next()

    print(primes.next())
