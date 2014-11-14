#!/usr/bin/env python

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        c = a
        a = a + b
        b = c

print sum([candidate for candidate in fibonacci(4e6) if candidate % 2 == 0])
