#(2n)!/n!

import numpy

n=21
a=numpy.zeros((n,n))

for i in range(1,n):
	a[0][i]=1
	a[i][0]=1

for i in range(1,n):
	for j in range(1,n):
		a[i][j]=a[i-1][j]+a[i][j-1]

print(a[20][20])
