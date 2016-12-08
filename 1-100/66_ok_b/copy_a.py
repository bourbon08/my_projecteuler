import math 
def gcd(a, b):
    if b == 0:
        return a
    else: 
        return gcd(b, a%b)
def solve(D):
    if int(math.sqrt(D)) == math.sqrt(D):
        return 0
    X = []
    x = int(math.sqrt(D))
    X.append(x)
    a = 1
    b = -x
    c = 1
    A = []
    B = []
    C = []
    A.append(a)
    B.append(b)
    C.append(c)
    g = 1
    while True:
        flag = 1
        for i in range(0, len(A)-1):
            # print a,A[i],b,B[i],c,C[i]
            if a == A[i] and b == B[i] and c == C[i]:
                flag = 0
                break
        if flag:
            t = abs(gcd(a, b))
            a /= t
            b /= t
            c *= t
            cc = a*a*D - b*b
            t = abs(gcd(c, cc))
            c /= t
            cc /= t
            x = c*(int(math.sqrt(D))*a - b)/cc
            X.append(x)
            aa = a*c
            bb = -c*b-x*cc
            a = aa
            b = bb
            c = cc
            A.append(a)
            B.append(b)
            C.append(c)
        else:
            break
 
    if (len(X)-1)&1:
        X.extend(X[1:-1])
        a = X[-1]
        b = 1
        for i in range(len(X)-2,-1,-1):
            t = a
            a = a*X[i]+b
            b = t
    else:
        a = X[-2]
        b = 1
        for i in range(len(X)-3,-1,-1):
            t = a
            a = a*X[i]+b
            b = t
    #print a,b,D,len(X)-1
    return a
    
if __name__ == "__main__":
    Max = 0
    D = 0
    for i in range(1,1001):
        t = solve(i)
        if t > Max:
            Max = t
            D = i
    print(Max, D)
