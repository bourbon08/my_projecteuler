from primesieve import *



ll=generate_primes(4,999999)
s={5,10,12,18,20,21,24}
t=0
while 1:
	try:
		p=ll[t];q=ll[t+1]
		if p==999983:
			break
	except:
		print(t,p)
		break
	
	for i in range(p*p+p,q**2,p):
		if (i%q)!=0:
			s.add(i)

	for i in range(q*q-q,p**2,-q):
		if (i%p) !=0:
			s.add(i)	
	
	t=t+1

ss=0
for i in s:
	if i <999966663333:
		ss=ss+i

print(ss)

