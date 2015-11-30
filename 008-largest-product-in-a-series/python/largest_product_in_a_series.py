#!/usr/bin/env python

import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', '..', 'python', 'lib')
sys.path.append(lib)

from util.functions import all_subseries


def main(series, quantity):
    subseries = all_subseries(series, quantity)
    products = filter(lambda s: not 0 in s, subseries)
    products = map(lambda l: reduce(lambda x, y: x*y, l), products)
    products.sort()
    return products.pop()

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print 'try with 1234567890 2'
        exit(1)

    series = int(args[0])
    quantity = int(args[1])

    print main(series, quantity)
