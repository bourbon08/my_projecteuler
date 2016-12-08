from primesieve import *

N=10**8
p=generate_primes(N)
ss=0

use=[]
for i in range(len(p)):
	p[i]=p[i]-1
	if p[i]%4 !=0 and p[i]%9 !=0:
		use.append(p[i])

q=generate_primes(N)



def BinarySearch(array,t):
    low = 0
    height = len(array)-1
    while low < height:
        mid = (low+height)//2
        if array[mid] < t:
            low = mid + 1
        elif array[mid] > t:
            height = mid - 1
        else:
            return array[mid]
    return -1

for i in use:
	flag=1
	for k in range(1,i//2+2):
		if i%k==0:
			if BinarySearch(q,k+i//k)==-1:
			#if k+i//k not in q:
				flag=0
				break
	if flag==1:
		#print(i)
		ss=ss+i


print(ss)
#print(use)
'''
for i in range(4,N+1):
	if i%2==1:
		continue
	
	if i in [100,1000,10000,10**5,10**6,10**7,10**7+5*10**6]:
		print(i)

	ll=fun(i)
	flag=1
	for j in ll:
		if j+i//j not in a:
			flag=0
			break

	if flag==1:
		ss=ss+i

print(ss)
'''
	
			