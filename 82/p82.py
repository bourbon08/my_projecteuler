import re
import copy

a = list()
a.append([0]*80)
for i in range(1,81):
    a.append([0])   #initialize matrix

    
f = open('p082_matrix.txt','r')
temp=1
for line in open('p082_matrix.txt'):
    #line = f.readline()
    match=re.findall(r'[0-9]+',line)
    for i in range(0,80):
        a[temp].append(int(match[i]))
    temp=temp+1


f.close()

MAXN = 1000 + 10

n=80
t=[0]*MAXN

for j in range(2,n+1):
    for i in range(1,n+1):
        t[i] = a[i][j] + a[i][j - 1]
    d=t[1]
    for i in range(2,n+1):
        d = d+ a[i][j]
        if d <= t[i]:
            t[i] = d
        else:
            d = t[i]
    d=t[n]
    for i in range(n-1,0,-1):
        d=d+a[i][j]  
        if d <= t[i]:
            t[i] = d
        else:
            d = t[i]
    for i in range(1,n+1):
        a[i][j]=t[i]


ans=a[1][80]
temp=0
for i in range(2,81):
    if a[i][80]<ans:
        ans=a[i][80]
        temp=i

print(ans,temp)
