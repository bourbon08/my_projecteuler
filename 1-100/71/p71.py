

a=3/7
temp=0
fenzi=0
for i in range(1,1000001):   #分母
	j=int(3*i/7)  			#分子
	if j/i > temp and j/i != a:
		temp=j/i
		fenzi=j

print(fenzi)

	