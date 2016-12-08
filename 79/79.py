




def fun(i,j):
	i=str(i);j=str(j)
	if j[0] in i:
		temp=i.find(j[0])
		if j[1] in i[temp:]:
			temp2=i.find(j[1])
			if j[2] in i[temp2:]:
				return 1
	return 0


s=10**7
ll=[319,680,180,690,129,620,762,689,318,368,710,720,629,168,160,716,731,736,769,290,719,389,162,289,718,790,890,362,760,316,729,380,728]

for i in range(s,10*s-1):
	flag=1
	for j in ll:
		if fun(i,j)==0:
			flag=0
			break
	
	if flag==1:
		print(i)
	