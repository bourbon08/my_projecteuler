import math
def panduan(p):
#a=3 b=-1 c= -2p
    n=(1+int(math.sqrt(1+24*p)))//6
    if (n*(3*n-1)//2) ==p :
        return True
    else:
        return False
    
   
a=[]
d=set()
for n in range(1,200003):
    a.append(n*(3*n-1)//2)


for i in range(200000):
    print(i,d)
    for j in range(i,200000):
        if a[i]!=a[j]:
            if panduan(a[i]+a[j]): 
                if panduan(abs(a[i]-a[j])):
                    d.add(abs(a[i]-a[j]))
                    print(i,j)
            
print(d)
        
        
        
#i,j=1019 2166
#     1560090 7042750
#d    548260