mx = 10000

primes = [2]

def isprime(p):
    for i in primes:
        if i * i > p:
            return True
        if p % i == 0:
            return False
    return True

x = 3
while x < mx:
    while not isprime(x):
        x += 2
    primes += [x]
    x += 2

ml = 10 ** 20

pairs = {a:{b for b in primes if a < b and isprime(int(str(a)+str(b))) and
            isprime(int(str(b)+str(a)))} for a in primes}

for a in primes:
    xa = pairs[a]
    for b in xa:
        xb = xa & pairs[b]
        for c in xb:
            xc = xb & pairs[c]
            for d in xc:
                xd = xc & pairs[d]
                for e in xd:
                    l = a + b + c + d + e
                    if l < ml:
                        ml = l

print(ml)