
count=0

b=1              #kong xin
while(1):
    z=b+2              #zhuang
    while(1):
        if z*z-b*b<=1000000:
            count+=1
            z+=2
        else:
            break
    b+=1
    if (b+1)*(b+1)-b*b>1000000:
        break
        
        
print(count)
        