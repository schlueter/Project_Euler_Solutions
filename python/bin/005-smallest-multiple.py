#!/usr/bin/env python

import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', 'lib')
sys.path.append(lib)

from util.functions import common_factors


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'try 20'
        exit(1)

    print(reduce(lambda x, y: x*y, common_factors(int(sys.argv[1]))))
