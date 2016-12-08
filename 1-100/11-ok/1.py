


f = open('date.txt','r')
result = list()
for line in open('date.txt'):
    line = f.readline()
    for i in range(0,20):result.append(int(line[3*i:3*i+2]))
print(len(result))
f.close()                

#上下
max=0
for i in range(0,20):
    for j in range(0,17):
        temp=result[i+20*j]*result[i+20*j+20]*result[i+20*j+40]*result[i+20*j+60]
        if temp>max:
            max=temp
            
#左右
for i in range(0,20):
    for j in range(0,17):
        temp2=result[j+20*i]*result[j+20*i+1]*result[j+20*i+2]*result[j+20*i+3]
        if temp2>max:
            max=temp2
#1
#  2
for i in range(0,17):
    for j in range(0,17):
        temp=result[i+20*j]*result[i+20*j+21]*result[i+20*j+42]*result[i+20*j+63]
        if temp>max:
            max=temp
#  2
#1        
for i in range(3,20):
    for j in range(0,17):
        temp=result[i+20*j]*result[i+20*j+19]*result[i+20*j+38]*result[i+20*j+57]
        if temp>max:
            max=temp





print(max)