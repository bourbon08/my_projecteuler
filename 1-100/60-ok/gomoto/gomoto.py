from erato import primes
from math  import sqrt
limit = 10**4
prime_set = primes(limit)
prime_limit_list  = sorted(prime_set)

def prime(a):
    if a == 1: return False
    if a == 2: return True
    if a % 2 == 0 or a % 3 == 0: return False
    return not any(a % x == 0 or a % (x+2) == 0 for x in range(5, int(sqrt(a))+1, 6))

def prime_pair(prime_list,prime_range):
    S = []
    for p in prime_list:
        s = set()
        for i in prime_range:
            if i != p:
                n1 = int(str(p)+str(i))
                n2 = int(str(i)+str(p))
                if prime(n1) and prime(n2):
                    s.add(i)
        S.append(s)
    return S

for p in prime_limit_list:
    Q = prime_set
    P = prime_pair([p],Q)
    for R in P:
        Q = Q & R
    for p1 in Q:
        Q1 = Q
        ps = {p,p1}
        if len(ps) > 1:
                P1 = prime_pair(ps,Q)
                for R1 in P1:
                    Q1 = Q1 & R1
                for p2 in Q1:
                    Q2 = Q1
                    ps2 = {p,p1,p2}
                    if len(ps2) > 2:
                            P2 = prime_pair(ps2,Q1)
                            for R2 in P2:
                                Q2 = Q2 & R2
                            for p3 in Q2:
                                Q3 = Q2
                                ps3 = {p,p1,p2,p3}
                                if len(ps3)>3:
                                        P3 = prime_pair(ps3,Q2)
                                        for R3 in P3:
                                            Q3 = Q3 & R3
                                        if Q3 != set():
                                            print(ps3 | Q3)
                                            print(sum(ps3 | Q3))
                                            exit()