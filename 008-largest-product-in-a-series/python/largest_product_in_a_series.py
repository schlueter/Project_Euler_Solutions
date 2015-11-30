#!/usr/bin/env python

import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
lib = os.path.join(realdir, '..', '..', 'python', 'lib')
sys.path.append(lib)

from util.functions import all_subseries


def main(series, quantity):
    sub_series = all_subseries(series, quantity)
    products = map(lambda l: reduce(lambda x, y: x*y, l), sub_series)
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
