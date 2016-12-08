import math
import time
 
start=time.time()
ll=[2,3]

def isPrime(n):
    if n <= 1:
        return False

    for i in ll:
        if n % i == 0:
            return False
        if i*i>n:
            break
    ll.append(n)
    return True
    
a=3
sum=5  

while(a<2000000):
    a+=2
    if(isPrime(a)):
        sum+=a;
    
    
print(sum)

end=time.time()
print('运行了'+str(end-start))  
	