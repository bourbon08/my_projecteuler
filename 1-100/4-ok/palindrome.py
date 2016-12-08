import itertools

def zz(n):
	weishu=len(str(n))
	l=''.join(x for x in str(n))
	for i in range(1,int(weishu/2)+1):
		if l[i-1]==l[weishu-i]:
			next
		else:
			return(False)
	return(True)
	

a=999
ll=[]
max=3
while(a>100):
	ll.append(a)
	a-=1
	
for b in list(itertools.permutations(ll,2)):
	if int(b[0]*int(b[1]))>max and zz(int(b[0]*int(b[1]))):
		print(int(b[0]*int(b[1])))
		max=int(b[0]*int(b[1]))