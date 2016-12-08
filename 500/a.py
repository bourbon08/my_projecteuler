import primesieve # pip install primesieve
import heapq

def solve(k, modulus=None):
    """Calculate the smallest number with 2**k divisors."""
    n = 1

    costs = primesieve.generate_n_primes(k) # more than necessary

    for i in range(k):
        cost = heapq.heappop(costs)
        heapq.heappush(costs, cost**2)
        n *= cost
        if modulus:
            n %= modulus

    return n

assert solve(4) == 120

if __name__ == "__main__":
    print(solve(500500, 500500507))