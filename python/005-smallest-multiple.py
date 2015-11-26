#!/usr/bin/env python

from sys import argv

from util.functions import common_factors


if __name__ == "__main__":
    print(reduce(lambda x, y: x*y, common_factors(int(argv[1]))))
