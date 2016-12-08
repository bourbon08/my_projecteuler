import itertools
import math
 
def isPrime(n):
    if n <= 1:
        return False
     
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
 
    return True
	
#def isPandigital(n):		#n is from 3 to 9

weishu=0


while True:
    a=[]
    if int((1+weishu)/2)%3==0: 
        weishu+=1
        next
    for x in range(1,weishu+1): a.append(x)
    
    for b in list(itertools.permutations(a,weishu)):
        if isPrime(int(''.join(str(x) for x in b)))==True: 
            print(b)
            break
    weishu+=1