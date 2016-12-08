from primesieve import *
import time
import math

f=open('a.txt','a')
t1=time.time()
mx = 10000
primesa = generate_primes(10000)
#primes_long=generate_primes(100000)

def isprime(n):
    if n <= 1:
        return 0
     
    for i in range(3, int(math.sqrt(n)) + 1,2):
        if n % i == 0:
            return 0
 
    return 1

def istwoPrime(m,n):
    if(isprime(int(''.join(str(m)+str(n)))) and isprime(int(''.join(str(n)+str(m))))):
        return 1
    return 0



ml = 10 ** 20

#pairs = {a:{b for b in primesa if a < b and isprime(int(str(a)+str(b))) and isprime(int(str(b)+str(a)))} for a in primesa}
pairs={}
for a in primesa:
    pairs[a]=[]
    for b in primesa:
        if(b>a and isprime(int(str(a)+str(b))) and isprime(int(str(b)+str(a)))):
            pairs[a]+=[b]
#i j k l m
found=0
for i in primesa:
    if found==1:
        break
    for j in pairs[i]:
        for k in pairs[j]:
            if istwoPrime(i,k):
                for l in pairs[k]:
                    if(istwoPrime(i,l) and istwoPrime(j,l)):
                        for m in pairs[l]:
                            if istwoPrime(i,m) and istwoPrime(j,m) and istwoPrime(k,m):
                                sum_m=sum([i,j,k,l,m])
                                found=1      

print(pairs[503][1])

f.write('p60')
f.write(str(sum_m))
print(ml)
t2=time.time()
f.write('cost'+str(t2-t1))
f.close()