#!/usr/bin/env python

import math
import sys


def main(target):
    b = int(target/2)

    while b > 0:
        a = 1
        while a < b:
            c_candidate = math.sqrt(a**2 + b**2)
            if c_candidate == int(c_candidate):
                c = c_candidate
                if a + b + c == target:
                    return a, b, c
            a = a + 1
        b = b - 1
    return -1, -1, -1

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 1:
        print 'try 1000'
        exit(1)

    target = int(args[0])

    triplet = main(target)
    solution = reduce(lambda x, y: x*y, triplet)
    print int(solution)
