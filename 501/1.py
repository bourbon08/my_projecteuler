def byz(n):
	a=2
	count=2
	for i in range(2,n):
		if n%i==0:count+=1
		if count>8:
			break		#important
	if count==8:
		return True
	else:
		return False
	
		
print(byz(24))
print(byz(88))
print(byz(11))

c=0
n=1
while(n<=1000000):
	if byz(n):
		c+=1
	n+=1
	
print(c)
