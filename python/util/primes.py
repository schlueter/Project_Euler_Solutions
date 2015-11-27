from sys import argv


class PrimeSieve:

    def __init__(self, initial_size):
        self.primes = [2]
        self.__calculate_primacies(range(3, initial_size, 2))

    def __calculate_primacies(self, candidates):
        for prime_candidate in candidates:
            prime = prime_candidate
            self.primes.append(prime)
            prime_index = candidates.index(prime)
            composite_candidates = candidates[prime_index + 1:]
            to_be_removed = filter(lambda x: x % prime == 0, composite_candidates)
            for candidate in to_be_removed:
                candidates.remove(candidate)

if __name__ == "__main__":
    print PrimeSieve(int(argv[1])).primes[int(argv[2])]
