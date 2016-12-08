from primesieve import *

p1=generate_primes(7090)
p2=generate_primes(369)
p3=generate_primes(85)
all=[]
count=0
for i in p1:
    print(i)
    for j in p2:
        for k in p3:
            temp=i**2+j**3+k**4
            if temp<=50000000 and temp not in all:
                all.append(temp)
                count+=1
print(count) 

f=open('p60','w')
f.write(str(count))
f.close()

               
            
            