import re
import copy

result1 = list()
result2=[]
for i in range(1,81):
    result1.append([])   #initialize matrix
    result2.append([0]*80)
    
f = open('p082_matrix.txt','r')
temp=0
for line in open('p082_matrix.txt'):
    #line = f.readline()
    match=re.findall(r'[0-9]+',line)
    for i in range(0,80):
        result1[temp].append(int(match[i]))
    temp=temp+1
    
f.close()

for i in range(80): 
    result2[i][0]=result1[i][0]

for i in range(0,80):   #hang
    for j in range(1,80): #lie
        if i==0:
            result2[i][j]=result1[i][j]+min(result2[i][j-1],result2[i+1][j-1]+result1[i+1][j])
        elif i==79:
            result2[i][j]=result1[i][j]+min(result2[i][j-1],result2[i-1][j-1]+result1[i-1][j])
        else:
            result2[i][j]=result1[i][j]+min(result2[i][j-1],result2[i-1][j-1]+result1[i-1][j],result2[i+1][j-1]+result1[i+1][j])


ans=result2[0][79]
temp=0
for i in range(80):
    if result2[i][79]<ans:
        ans=result2[i][79]
        temp=i

print(ans,i)



'''
result3=copy.copy(result2)
#for i in range(1,80):
#    result2[i]=result1[1][80*(i-1):80*(i-1)+80]
    
#result2 is what we need

for i in range(1,80):
    for j in range(80): #hang
        if j==0:
            result3[j][i]=min(result2[j][i]+result3[j][i-1],result2[j+1][i]+result3[j+1][i-1]+result2[j][i])      
        elif j==79:
            result3[j][i]=min(result2[j][i]+result3[j][i-1],result2[j-1][i]+result3[j-1][i-1]+result2[j][i]) 
        else:
            result3[j][i]=min(result2[j+1][i]+result3[j+1][i-1]+result2[j][i],result2[j][i]+result3[j][i-1],result2[j-1][i]+result3[j-1][i-1]+result2[j][i])
ans=result3[0][79]
for i in range(80):
    if result2[i][79]<ans:
        ans=result2[i][79]
        
print(ans)
'''
        

  