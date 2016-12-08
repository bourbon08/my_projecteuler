import math
import time
start=time.time()
def yueshu(n):
    count=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            count+=2
    return count
    
a=3
b=3
while(1):
    if yueshu(a)>=500:
        print(a)
        break
    a+=b
    b+=1
    
end=time.time()
print(str(end-start))
