maxb=0
maxn=0
ll=[0]*(10**9+1)
for i in range(10,1000000):
	temp=i
	count=0
	while i !=1:
		if i <10**9+1:
			if ll[i]!=0:
				count=count+ll[i]
				break
		if i%2==0:
			i=i//2
		else:
			i=3*i+1
		
		count=count+1
	ll[i]=count
	
	if count>maxb:
		maxb=count
		maxn=temp

print(maxb,maxn)
