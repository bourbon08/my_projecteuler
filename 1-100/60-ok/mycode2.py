from itertools import *
import math

def isPrime(n):
    if n <= 1:
        return 0
     
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
 
    return 1

def istwoPrime(m,n):
    if(isPrime(int(''.join(str(m)+str(n)))) and isPrime(int(''.join(str(n)+str(m))))):
        return 1
    return 0

ll=[2]
found=0
for temp in range(3,10000):
	if isPrime(temp):ll.append(temp)
count=0
for i in combinations(ll,3):
    if(istwoPrime(i[0],i[1]) and istwoPrime(i[0],i[2]) and istwoPrime(i[1],i[2])):
        count+=1
print(count) 
'''
ll=[2]
found=0
for temp in range(3,10000):
	if isPrime(temp):ll.append(temp)
    
for i in combinations(ll,5):
    count=0
    if(found==1):
        break
    for j in combinations(i,2):
        if(istwoPrime(j[0],j[1])):
            count+=1
        if(count==10):
            print(str(sum(i)))
            found=1
'''
        