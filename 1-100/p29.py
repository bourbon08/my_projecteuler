ll=[]

for i in range(2,101):
     for j in range(2,101):
         ll.append(i**j)

print(set(ll))