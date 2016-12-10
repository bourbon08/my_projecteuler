def factor(n):
    """returns the largest factor of n"""
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return factor(n / i);
    return n

def totient(n):
    tot = n;
    while(n > 1):
        f = factor(n)
        tot -= tot / f
        while(n % f == 0):
            n /= f
    return tot

lut = {}
def farey(n):
    """ compute the length of the farey sequence of order n """
    if n in lut:
        return lut[n]
    r = (n * (n + 3)) / 2
    d = 2
    while(d <= n):
        p = n / d
        next = n / p
        k = farey(p)
        r -= (next - d + 1) * k
        d = next + 1
    lut[n] = r
    return r

def S(n,m):
    if m == 0 or n == 0: return 0
    if m == 1: return totient(n)
    if n == 1: return farey(m) - 1

    p = factor(n)
    q = n / p
    r = (p - 1) * S(q, m)
    return r + S(n, m / p)

print("Answer:", S(510510, 10 ** 11))