import time
t=time.time()
value = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

coin_combos = [1] + [0] * value
for coin in coins:
    for i in range(coin, value + 1):
        coin_combos[i] += coin_combos[i - coin]%(10**9+7)

ans = coin_combos[value]%(10**9+7)
print(ans)



print(time.time()-t)