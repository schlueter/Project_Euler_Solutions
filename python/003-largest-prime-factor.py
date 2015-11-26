#!/usr/bin/env python

import sys

from util.generators import set_of_prime_factors


print(set_of_prime_factors(int(sys.argv[1])).next())
