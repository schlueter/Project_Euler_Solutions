#!/usr/bin/env python

import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', '..', 'python', 'lib')
sys.path.append(lib)

from util.generators import primes_from_sieve


def main(target):
    primes = primes_from_sieve(target)

    return sum(primes)

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 1:
        print "try 2000000"
        sys.exit(1)

    target = int(args[0])
    print main(target)
