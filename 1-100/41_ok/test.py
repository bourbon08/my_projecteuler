import itertools
import math
 
def isPrime(n):
    if n <= 1:
        return False
     
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
 
    return True
	

a=[7,6,5,4,3,2,1]
max=0
for b in list(itertools.permutations(a,7)):
	c=int(''.join(str(x) for x in b))
	if isPrime(c)==True: 
		if c>max:
			print(c)
			max=c
