import math


def factors(i):
    p = math.floor(math.sqrt(i))
    while p > 0:
        if not i % p:
            yield int(p)
        p = p - 1

def set_of_prime_factors(i):
    for f in factors(i):
        if factors(f).next() == 1:
            yield f

def prime_numbers():
    primes = [2]
    while True:
        yield primes[-1]
        candidate = primes[-1] + 1
        candidate_filter = lambda x: candidate % x == 0
        while filter(candidate_filter, primes):
            candidate = candidate + 1
        primes.append(candidate)

def primes_from_sieve(max):
    prime = 2
    yield prime
    candidates = range(3, max, 2)
    while prime < math.sqrt(max):
        prime = candidates.pop(0)
        yield prime
        candidates = filter(lambda x: x % prime != 0, candidates)
    for candidate in candidates:
        yield candidate

def integer_factorization(i):
    primes = primes_from_sieve(i + 1)
    prime = primes.next()
    while i != 1:
        if not i % prime:
            yield prime
            i = i/prime
        else:
            prime = primes.next()
