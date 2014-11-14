#!/usr/bin/env python

fib = [1,2]
ans = 0

while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])

for i in fib:
    if i % 2 == 0:
        ans += i

print ans
