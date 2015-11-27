from sys import argv


class PrimeSieve:

    def __init__(self, initial_size):
        self.primes = [2]
        self.__calculate_primacies(range(3, initial_size, 2))

    def __calculate_primacies(self, candidates):
        while candidates:
            prime = candidates.pop(0)
            self.primes.append(prime)
            candidates = filter(lambda x: x % prime != 0, candidates)

if __name__ == "__main__":
    print PrimeSieve(int(argv[1])).primes[int(argv[2])]
