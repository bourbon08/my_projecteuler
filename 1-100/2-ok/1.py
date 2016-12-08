a=1
b=2
sum=2
while(b<4000000):
	c=a+b
	if(c%2==0):
		sum+=c
	a=b
	b=c
	
print(sum)