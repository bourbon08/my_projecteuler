import math

def isPrime(n):   
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return n//i
    return n
    
t = int(input().strip())
a = []
for a_i in range(t):
    a.append(int(input()))
    if a[a_i]>1000000000000:
        a[a_i]=1000000000000
for i in range(t):
    print(isPrime(a[i]))
    