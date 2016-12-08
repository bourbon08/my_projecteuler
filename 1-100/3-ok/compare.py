import math
def mys(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return n//i
    return n

def otherss(n):
    i = 2
    largest_prime = 2
    while i*i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i    
        i += 1
    if n>largest_prime:
        largest_prime = n;
    return largest_prime
    
for i in range(1000):
    if mys(i)!=otherss(i):
        print(str(i)+" "+str(mys(i))+" "+str(otherss(i)))