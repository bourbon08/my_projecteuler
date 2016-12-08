#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import math
 
#
# See:
# http://en.wikipedia.org/wiki/Chakravala_method#The_method
# http://kappadath-gopal.blogspot.com/2013/04/ancient-medieval-indian-mathematics.html
# http://jwb.io/20121231-the-euclidean-algorithm-and-chakravala-method-in-ruby.html
#
def chakravala(N):
   
    m = m0 = int(round(math.sqrt(N)))
    a, b, k = m, 1, m*m - N
    if k == 0:
        # no solution if N is a perfect square
        return (None, None)
 
    while k != 1:
        # terminate if k in [-1, ±2], or k is ±4 and a or b is even
        if k == -1 or abs(k) == 2 or (abs(k) == 4 and not (a&1 and b&1)):
            # compose (a, b, k) with (a, b, k) and return solution
            return ((a*a + N*b*b)//abs(k), 2*a*b//abs(k))
 
        # find m such that: (a + b*m) % k == 0, abs(m^2 - N) is minimized
        diff = (m + m0) % abs(k)
        m_lo = m0 - diff
        m_hi = m_lo + abs(k)
        m = m_hi if abs(m_hi*m_hi - N) < abs(m_lo*m_lo - N) else m_lo
 
        # compose (a, b, k) with (m, 1, m^2 - N)
        a, b, k = (m*a + N*b)//abs(k), (a + b*m)//abs(k), (m*m - N)//k
    return (a, b)
 
if __name__ == "__main__":


    max_i=0
    max_x=0
    ll=[]
    for i in range(2,33):
        ll.append(i*i)


    for i in range(10,1001):
        if i in ll:
            continue
        x=chakravala(i)[0]
        if x>max_x:
            max_x=x
            max_i=i

    print(max_i)  