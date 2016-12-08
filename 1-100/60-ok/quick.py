from itertools import combinations
import time

aaa=time.time()

def is_prime(n):
  " poor is_prime function "
  if n<4: return n>1
  if not n%2: return False
  for p in range(3, n, 2):
    if p*p>n: return True
    if not n%p: return False

def PE060():
  F={}
  res5=float('inf')
  res4=792 # officiel !!!
  res3=119 # 
  i=0
  set4=set()
  ti=10
  prime = []
  pi = 1
  while True:
    pi+=2
    comp = False
    for p in prime:
      if p*p>pi:
        break
      if not pi%p:
        comp = True
        break
    if comp: continue
    prime.append(pi) # pi is prime
    if ti<pi: ti*=10
    F[i]=set()
    pimod3= pi%3
    pq=10*pi+3
    qp=3*ti+pi
    # a pseudo prime test is done in order to eliminate most of candidates
    if pq%5 and qp%5 and pq%7 and qp%7\
    and pq%11 and qp%11 and pq%13 and qp%13 and pq%17 and qp%17\
    and pq%19 and qp%19 and pq%23 and qp%23 and pq%27 and qp%27\
    and pq%31 and qp%31 and pq%37 and qp%37 and pq%39 and qp%39\
    and (pow(2, pq-1, pq)==1) and (pow(2, qp-1, qp)==1):
        F[i].add(0)
        F[0].add(i) # 3 est d'indice 0
    tj=10
    for j in range(1,i):
      pj=prime[j]
      if pj%3-pimod3: continue # pi et pj doivent avoir la m��me congruence mod 3, sauf si c'est 3
      if tj<pj: tj*=10
      pq=pi+pj*ti
      qp=pj+pi*tj
      if pq%5 and qp%5 and pq%7 and qp%7\
      and pq%11 and qp%11 and pq%13 and qp%13 and pq%17 and qp%17\
      and pq%19 and qp%19 and pq%23 and qp%23 and pq%27 and qp%27\
      and pq%31 and qp%31 and pq%37 and qp%37 and pq%39 and qp%39\
      and (pow(2, pq-1, pq)==1) and (pow(2, qp-1, qp)==1):
        F[i].add(j)
        F[j].add(i)
    for j in F[i]:
      pj=prime[j]
      if pi+pj+res3<res5:
        F[i, j] = F[i] & F[j]
        for k in F[i, j]:
          pk=prime[k]
          if k<j and pk+pj+pi+10<res5: # 3+7->10
            F[i,j,k] = F[i, j] & F[k]
            for l in F[i, j, k]:
             pl=prime[l]
             if l<k and pi+pj+pk+pl+3<res5:
              m = F[i, j, k] & F[l]
              if m:
                if min(m)<l:
                  pm=prime[min(m)]
                  # We make a deterministic prime test to confirm !!!
                  if all(is_prime(int(str(p)+str(q))) and \
                           is_prime(int(str(q)+str(p)))   \
                           for p,q in combinations({pi, pj, pk, pl, pm}, 2)):
                   res5=min(res5, pi+pj+pk+pl+pm)
                  print(sum([pi, pj, pk, pl, pm]),"avec", (pi, pj, pk, pl, pm))
    if pi+res4>res5: return res5
    i+=1
    
PE060()

bbb=time.time()
print(bbb-aaa)