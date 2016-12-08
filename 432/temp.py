cache={}
cache[1]=1
def S1(n):
	if n in cache:
		return cache[n]
	else:
		s=(n*(n+1))/2
		k=1
		while k*(k+1)<n:
			s-=(S1(k)*((n/k)-(n/(k+1))))
			k+=1
		d=n/k
		while d>1:
			s-=S1(n/d)
			d-=1
		cache[n]=s
		return s

# S(L,n) = S(k,n) where L is the list
# of the prime factors of k.

def S(L,n):
	if L==[]:
		return S1(n)
	else:
		if n==0:
			return 0
		else:
			return (L[0]-1)*S(L[1:],n)+S(L,n/L[0])


answer = S([2,3,5,7,11,13,17],10**4)

print("Full answer : "+str(answer))
print("Modulo 10**9 : "+str(answer%(10**9)))