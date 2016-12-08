import math
 
def isPrime(n):
    if n <= 1:
        return False
     
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
 
    return True

n=2
count=0
while True:
	if isPrime(n)==True: count=count+1
	
	if count==10001: 
		print(n)
		break
	n+=1
	
