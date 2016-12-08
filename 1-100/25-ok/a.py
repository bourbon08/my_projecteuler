a=1
b=1
count=2
while True:
    he=a+b
    count+=1
    if he>=10**999:
        print(count)
        break
    a=b
    b=he
    