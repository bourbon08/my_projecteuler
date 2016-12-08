
l2=[0]*57

l2[2]=1
l2[3]=2
for i in range(4,52):
	for j in range(0,i-2+1):
		l2[i]=l2[i]+l2[j]+1
	




l3=[0]*57
l3[3]=1
l3[4]=2
for i in range(5,52):
	for j in range(0,i-3+1):
		l3[i]=l3[i]+l3[j]+1

l4=[0]*57
l4[4]=1
l4[5]=2
for i in range(6,52):
	for j in range(0,i-4+1):
		l4[i]=l4[i]+l4[j]+1

t=50
print(l2[t]+l3[t]+l4[t])


#easy