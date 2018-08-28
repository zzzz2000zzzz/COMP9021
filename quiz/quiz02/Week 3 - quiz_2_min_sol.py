# Prompts the user for an integer N at least equal to 5,
# computes the largest number l >= 1 such that l consecutive prime numbers
# add up to a prime number at most equal to N,
# and outputs l and the largest such prime number.
#
# Written by Eric Martin for COMP9021


from math import sqrt
import sys


def solution(N):
    primes_sieve = [True] * (N + 1)
    for n in range(2, round(sqrt(N)) + 1):
        if primes_sieve[n]:
            for i in range(n * n, N + 1, n):
                primes_sieve[i] = False
    primes = [0] + [i for i in range(2, len(primes_sieve)) if primes_sieve[i]]
    largest_prime = None
    total_sum = sum(primes[: -2])
    end = -3
    for max_length in range(len(primes) - 2, 0, -1):
        candidate = total_sum
        for i in range(len(primes) - max_length - 1):
            candidate = candidate - primes[i] + primes[i + max_length]
            if candidate > N:
                break
            if primes_sieve[candidate]:
                largest_prime = candidate
        if largest_prime:
            return max_length, largest_prime
        total_sum -= primes[end]
        end -= 1
    return None, None
  
try:
    N = int(input('Enter an integer at least equal to 5: '))
    if N < 5:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

max_length, largest_prime = solution(N)
if max_length:
    print('The largest sequence of consecutive primes that add up\n  '
          'to a prime P equal to {} at most has a length of {}.\n'
          'The largest such P is {}.'.format(N, max_length, largest_prime))
            
