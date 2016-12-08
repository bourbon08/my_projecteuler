t = int(input().strip())
a = []
for a_i in range(t):
    a.append(int(input()))
    
i = 1
for temp in range(t):
    i=1
    for k in (range(1, a[temp]+1)):
        if i % k > 0:
            for j in range(1, a[temp]+1):
                if (i*j) % k == 0:
                    i *= j
                    break
    print(i)

#可以优化