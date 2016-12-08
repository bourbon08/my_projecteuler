
n=int(input())
a_t=[]
for i in range(n):
    temp=int(input())
    a_t.append(temp)
for i in range(n):
    value = a_t[i]
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    coin_combos = [1] + [0] * value
    for coin in coins:
        for i in range(coin, value + 1):
            coin_combos[i] =(coin_combos[i]+ coin_combos[i - coin])
            coin_combos[i]=coin_combos[i]%(10**9+7)
            

    ans = coin_combos[value]%(10**9+7)
    print(ans)