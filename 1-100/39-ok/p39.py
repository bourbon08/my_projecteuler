'''l=[ 0 for i in range(10001)]

    
for u in range(33):
    for v in range(u,33):
        a=u*u-v*v
        b=2*u*v
        c=u*u+v*v
        if a+b+c<1000:
            l[a+b+c]+=1
print(l)
            
            
big=0
temp=0
for i in range(10001):
    if l[i]>temp:
        big=i
        temp=l[i]
print(big)
'''
big=0
temp=0
l=[ 0 for i in range(1000)]
for i in range(12,1000):
    for a in range(1,i):
        for b in range(a,i):
            c=i-a-b
            if a*a+b*b==c*c:
                l[i]+=1
    if l[i]>temp:
        big=i
        temp=l[i]
    print(big)
                
                
print(big)
              
              
    
    

            