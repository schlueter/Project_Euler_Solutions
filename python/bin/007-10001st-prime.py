#!/usr/bin/env python

import math
import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', 'lib')
sys.path.append(lib)

from util.generators import prime_numbers
from util.generators import primes_from_sieve


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 1:
        print "try 10001"
        sys.exit(1)

    target = int(args.pop())

    max_prime_estimate = int(target * math.log(target) * 1.5)
    primes = primes_from_sieve(max_prime_estimate)
    for i in xrange(target - 1):
        primes.next()
    print(primes.next())
