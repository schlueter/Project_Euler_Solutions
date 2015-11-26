#!/usr/bin/env python

import math
import sys


def factors(i):
    p = math.floor(math.sqrt(i))
    while p > 0:
        if i % p == 0:
            yield int(p)
        p = p - 1

    return

def prime_factors(i):
    for f in factors(i):
        if factors(f).next() == 1:
            yield f
    return

print(prime_factors(int(sys.argv[1])).next())
