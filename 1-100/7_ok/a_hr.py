import math

def isPrime(n):
    if n <= 1:
        return False     
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
t = int(input().strip())
a = []
for a_i in range(t):
    a.append(int(input()))
b=[2]
n=3
count=1
while True:
    if isPrime(n): 
        count=count+1
        b.append(n)	
    if count==10001: 
        break
    n+=2
    
for i in range(t):
    print(b[a[i]-1])