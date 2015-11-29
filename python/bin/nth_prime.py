#!/usr/bin/env python

import math
import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', 'lib')
sys.path.append(lib)

from util.generators import primes_from_sieve


def main(target):

    max_prime_estimate = int(target * math.log(target) * 1.5)
    primes = primes_from_sieve(max_prime_estimate)
    for i in xrange(target - 1):
        primes.next()

    return primes.next()

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 1:
        print "try 10001"
        sys.exit(1)

    target = int(args.pop())
    print main(target)
