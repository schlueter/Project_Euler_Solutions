from generators import integer_factorization


def common_factors(target):
    factors = {}

    for n in xrange(2, target + 1):
        factors_of_n = [factor for factor in integer_factorization(n)]
        for factor in set(factors_of_n):
            if factors_of_n.count(factor) > factors.get(factor, 0):
                factors[factor] = factors_of_n.count(factor)

    return [f for f in factors.keys() for x in xrange(factors[f])]
