t=int(input())
ll=[]
def SumD(m,n):
    p=int(m/n)
    return n*p*(p+1)/2
for i in range(t):
    ll.append(int(input()))
for i in range(t):
     
    print(int(SumD(ll[i],3)+SumD(ll[i],5)-SumD(ll[i],15)))