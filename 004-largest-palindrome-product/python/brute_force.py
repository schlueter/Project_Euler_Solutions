#!/usr/bin/env python

import sys


def is_string_palindrome(candidate):
    if len(candidate) == 1:
        return True
    elif len(candidate) == 2 and candidate[0] == candidate[1]:
        return True
    elif candidate[0] == candidate[-1]:
        return is_string_palindrome(candidate[1:-1])
    return False

def pairs_down(start):
    for a in xrange(1, start):
        for b in xrange(1, a):
            yield a, b
    return

palindromes = []
for p in pairs_down(int(sys.argv[1])):
    product = int.__mul__(*p)
    if is_string_palindrome(str(product)):
        palindromes.append(product)

palindromes.sort()
print(palindromes.pop())
