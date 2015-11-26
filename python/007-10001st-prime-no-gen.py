#!/usr/bin/env python

from sys import argv

from util.functions import nth_prime


if __name__ == "__main__":
    target = int(argv[1])
    print(nth_prime(target))
