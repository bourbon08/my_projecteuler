def expMod2(x,y,k):
	#快速幂取模
	#http://blog.csdn.net/on_1y/article/details/7989603
	tx = x
	modRes = 1  
	tx = tx%k
	while(y):
		if (y&1):
			modRes = modRes * tx % k
		y = (y>>1)
		tx = tx * tx % k
	return modRes



a=int(input())

t=0
for j in range(1,a[i]+1):
	t=(t+expMod2(j,j,10**10))%(10**10)
print(t)

