#!/usr/bin/env python

from sys import argv

if __name__ == "__main__":
    target = int(argv[1])

    sum_of_squares = sum([ n**2 for n in xrange(target + 1)])
    square_of_sums = sum([ n for n in xrange(target + 1)])**2

    print(square_of_sums - sum_of_squares)
