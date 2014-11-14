#!/usr/bin/env python

def fib(max):
    pair = (0, 1)
    while sum(pair) < max:
        yield pair[0]
        pair = (sum(pair), pair[0])

print sum([candidate for candidate in fib(4e6) if candidate % 2 == 0])
