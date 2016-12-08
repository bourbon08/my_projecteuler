def funsum(n):
    a=1
    b=2
    sum=2
    c=a+b
    while(c<=n):
        if c%2==0:
            sum+=c
        a=b
        b=c
        c=a+b
    return sum
        
t=int(input())
a=[]
for i in range(t):
    a.append(int(input()))
for i in range(t):
    print(funsum(a[i]))