from generators import integer_factorization


def common_factors(target):
    factors = {}

    for n in xrange(2, target + 1):
        factors_of_n = [factor for factor in integer_factorization(n)]
        for factor in set(factors_of_n):
            if factors_of_n.count(factor) > factors.get(factor, 0):
                factors[factor] = factors_of_n.count(factor)

    return [f for f in factors.keys() for x in xrange(factors[f])]

def nth_prime(n):
    primes = [2]
    for p in range(n - 1):
        candidate = primes[-1] + 1
        candidate_filter = lambda x: candidate % x == 0
        while filter(candidate_filter, primes):
            candidate = candidate + 1
        primes.append(candidate)
    return primes[-1]

def all_subseries(series, quantity):
    list_of_all_subseries = []
    while series > 10**quantity:
        subseries = []
        for i in range(quantity):
            subseries.append(series / 10**i % 10)
        series = series / 10
        list_of_all_subseries.append(subseries)
    return list_of_all_subseries
