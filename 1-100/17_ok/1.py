
ge=[0,3,3,5,4,4,3,5,5,4]    #one two three four five six seven eight nine
shi1=[3,6,6,8,8,7,7,9,8,8]  #ten,Eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,
shi2=[0,0,6,6,5,5,5,7,6,6]  #twenty,Thirty, forty, fifty, sixty, seventy, eighty, ninety
sum=0
for i in range(1,1000):
    if int(i/100)>=1:
        sum+=ge[int(i/100)]+7
        if i%100>0:
            sum+=3
            
    temp=i%100
    if temp<20 and temp>9:
        sum+=shi1[temp-10]
    else:
        if i%100<10:
            sum+=ge[i%100]
        else:
            sum+=shi2[int(i%100/10)]
            sum+=ge[i%10]
        
sum+=11         
print(sum)
    
        