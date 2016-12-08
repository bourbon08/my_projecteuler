def sieve(s,n=None):
    if not n:
        n = s
        s = 2
    sieve = [True] * n
    for i in (i for i in range(3,int(n**0.5)+1,2) if sieve[i]):
        sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return ([2] if s <= 2 else []) + [i for i in range(2*(s//2)+1,n,2) if sieve[i]]

primes = sieve(10**4)
primes_squared = [p**2 for p in primes]
primes_strings = [str(p) for p in primes]
primes_sum_mod = [sum(map(int,p)) % 3 for p in primes_strings]
L = len(primes)

def is_both_prime(i,j):
    if (primes_sum_mod[i] + primes_sum_mod[j]) % 3 == 0:
        return False
    p, q = int(primes_strings[i]+primes_strings[j]), int(primes_strings[j]+primes_strings[i])
    if i == 2 or j == 2 or p % 7 == 0 or q % 7 == 0 or p % 11 == 0 or q % 11 == 0 or p % 13 == 0 or q % 13 == 0:
        return False
    if p > q:
        p, q = q, p
    ind_p, ind_q = bisect_right(primes_squared, p), bisect_right(primes_squared, q)
    for r in primes[6:ind_p]:
        if p % r == 0 or q % r == 0:
            return False
    for r in primes[ind_p:ind_q]:
        if q % r == 0:
            return False
    return True

prime_twins = [{j for j in range(1,i) if is_both_prime(i,j)} for i in range(L)]

def find_family():
    for e in range(5,L):
        for d in prime_twins[e] - {1,3}:
            for c in (prime_twins[d] & prime_twins[e]) - {1}:
                for b in (prime_twins[c] & prime_twins[d] & prime_twins[e]) - {1}:
                    for a in prime_twins[b] & prime_twins[c] & prime_twins[d] & prime_twins[e]:
                        return [primes[x] for x in [a, b, c, d, e]]
prime_list = find_family()
print('The family '+str(prime_list)+', which sums to '+str(sum(prime_list)))