
import itertools  
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
        
sum=0
ll=[2]
found=0
for i in range(3,10000):
	if isPrime(i):ll.append(i)
    
for i1 in range(1229):
    for i2 in range(i1+1,1229):
        if(istwoPrime(ll[i1],ll[i2])):
            for i3 in range(i2+1,1229):
                if(istwoPrime(ll[i1],ll[i3]) and istwoPrime(ll[i2],ll[i3]) ):
                    for i4 in range(i3+1,1229):
                        print(ll[i4])
                        if(istwoPrime(ll[i1],ll[i4]) and istwoPrime(ll[i2],ll[i4]) and istwoPrime(ll[i3],ll[i4])):
                            for i5 in range(i4+1,1229):
                                if(istwoPrime(ll[i1],ll[i5]) and istwoPrime(ll[i2],ll[i5]) and istwoPrime(ll[i3],ll[i5]) and istwoPrime(ll[i4],ll[i5])):
                                    if(ll[i1]+ll[i2]+ll[i3]+ll[i4]+ll[i5]>sum):
                                        sum=ll[i1]+ll[i2]+ll[i3]+ll[i4]+ll[i5]
            
'''   
for i in range(5,len(ll)):
    for j in list(itertools.permutations(ll[0:i],3)):
        temp=0
        for k in list(itertools.permutations([j[0],j[1],j[2],ll[i]],2)):
            if isPrime(int(''.join(str(x) for x in k)))==0:
                break
            else:
                temp=temp+1
        if temp==12:
            print(ll[j[0]],ll[j[1]],ll[j[2]],ll[j[3]],ll[i])
            found=1
            break
    print(i)
    if found==1:
        break
'''

f=open('a.txt','w')
f.write(str(sum))
f.close()

        
        
                
	

