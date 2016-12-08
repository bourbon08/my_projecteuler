import re

result = list()
for i in range(1,81):
    result.append([])   #initialize matrix
    
f = open('p081_matrix.txt','r')
temp=0
for line in open('p081_matrix.txt'):
    line = f.readline()
    match=re.findall(r'[0-9]+',line)
    for i in range(0,80):
        result[temp].append(match[i])
    temp=+1
    
print(len(result))
f.close()  