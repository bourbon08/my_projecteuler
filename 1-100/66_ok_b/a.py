import math
def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, int(math.sqrt(d))
 
    while k != 1 or y == 0:
        p = k * (p/k+1) - p
        p = p - int((p - sd)/k) * k
 
        x = (p*x1 + d*y) / abs(k)
        y = (p*y + x1) / abs(k)
        k = (p*p - d) / k
        x1 = x
    return x
    
print(pell(61))