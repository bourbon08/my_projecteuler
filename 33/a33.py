
for i in range(10,100):
    for j in range(10,100):
        if i/j>=1:
            continue
        try:
            if i/j in [(i%10)/(j%10),(i%10)/(int(j/10)),(int(i/10))/(j%10),(int(i/10))/(int(j/10))]:
                print(i,j)
        except:
            continue