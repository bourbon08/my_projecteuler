import itertools as iter 
import math

def isPrime(n):
    if n <= 1:
        return 0
     
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
 
    return 1
    
def make_chain(chain):
    if len(chain) == set_size:
        return chain 
    for p in primes:
        if p > chain[-1] and all_prime(chain+[p]):
            new_chain = make_chain(chain+[p])
            if new_chain:
                return new_chain
    return False 

def all_prime(chain):
    return all(isPrime((p[0]) + (p[1])) for p in iter.permutations(chain, 2))
    
set_size = 5
primes=[2]
found=0
for temp in range(3,10000):
	if isPrime(temp):primes.append(temp)
    
chain = 0
while not chain:
    chain = make_chain([primes.pop(0)])

print("Project Euler 60 Solution =", sum(map(int, chain)), chain)
 
