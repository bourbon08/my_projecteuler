import time
from primesieve import *
t=time.time()
def weiyi(value,coins):
    #value = 200
    #coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coin_combos = [1] + [0] * value
    for coin in coins:
        for i in range(coin, value + 1):
            coin_combos[i] += coin_combos[i - coin]
    return coin_combos[value]
temp=10  
while(True):
    #print(temp)
    if(weiyi(temp,generate_primes(temp))>=5000):        
        print(temp)
        break
    temp+=1
    
    
    



print(time.time()-t)