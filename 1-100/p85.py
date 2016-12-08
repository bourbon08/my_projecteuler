

def fun(p,q):
	count=0
	for i in range(1,p+1):
		for j in range(1,q+1):
			count=count+(p-i+1)*(q-j+1)
	return count

ll=[]

for a in range(1,100):
	for b in range(1,100):
		if fun(a,b)>2000000:
			ll.append(a*b)

print(min(ll))