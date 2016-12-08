from allfunction import *

def quadratic_formula(a,b):
    n=0
    count=0
    while True:
        if(isPrime(n*n+a*n+b)):
            count+=1
            n+=1
        else:
            break
    return count
            
t1=t2=0
t3=t4=0
for i in range(-999,1000):
    for j in range(-999,1000):
        qf=quadratic_formula(i,j)
        if qf>t1:
            t1=qf
            t2=i*j
            t3,t4=i,j
            
            
print(t2,t3,t4)
            
        
        