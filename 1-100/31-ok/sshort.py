def Sol(money,coinlist):
    if len(coinlist) == 1:
        return 1
    sum = 0;
    for i in range(len(coinlist)):
        if money-coinlist[i] == 0:
            sum += 1
        elif money-coinlist[i] > 0:
            sum += Sol(money-coinlist[i],coinlist[i:])   #or coinlist[:i+1]
    return sum
print(Sol(200,[1,2,5,10,20,50,100,200]))
