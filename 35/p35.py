import primesieve
from allfunction import *

def shengcheng(n):
    if len(str(n))==1:
        return [n]
    

count=0
a=primesieve.generate_primes(1000000)
isprimelist=[False for _ in range(1000001)]
for i in a:
    isprimelist[i]=True


for p in a:
    
    #b=num2list(p)
    l = len(str(p))
    h = 10 ** (l - 1)
    flag = True
    t = p
    for i in range(1, l):
        t = t // 10 + t % 10 * h
        if not isprimelist[t]:
            flag = False
            break
    if flag:
        print(p)
        count+=1
    '''
    flag=1
    temp=QPL2(b)

    for j in temp:
        if not isprimelist[j]:
            flag=0
      
    if flag==1:
        count+=len(temp)
        print(a[jishu])
    '''
        
        
        
print(count)
    
        
    
    