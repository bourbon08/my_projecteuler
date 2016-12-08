from math import sqrt

def primes(n):
        limit = n
        r = range(1,limit)
        prime = [True]*limit
        primes = set()
        prime[1]= False
        for i in range(2,int(sqrt(limit)+1)):
                if prime[i]:
                        for j in range(i*i,limit,i):
                                prime[j] = False

        for i in range(1,limit):
                if prime[i]:
                        primes.add(i)
        return primes