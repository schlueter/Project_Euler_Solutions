#!/usr/bin/env python

import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', 'lib')
sys.path.append(lib)

from util.functions import nth_prime


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'try 10001'
        exit(1)

    target = int(sys.argv[1])
    print(nth_prime(target))
