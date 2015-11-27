#!/usr/bin/env python

import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', 'lib')
sys.path.append(lib)

from util.generators import set_of_prime_factors


if __name__ == '__main__':

    args = sys.argv[1:]

    if len(args) != 1:
        print "try 600851475143"
        sys.exit(1)

    target = int(args.pop())

    print(set_of_prime_factors(target).next())
