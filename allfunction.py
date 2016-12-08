import itertools
import math

def list2num(n):
    #list2num([1,2,3]) -> 123
    return int(''.join(str(temp) for temp in n))
    
def num2list(n):
    #num2list(123) -> [1,2,3]
    a=[]
    for i in str(n):
        a.append(int(i))    
    return a

def gcd(a,b):
    while 1:
        r=a%b
        if not r:
            return b
        a=b
        b=r
         
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def QPL(m_list):        #返回m_list的全排列        
    if len(m_list) == 1:
        yield m_list
    for i in range(len(m_list)):
        restlist = m_list[0:i]+m_list[i+1:]
        for subres in QPL(restlist):
            yield [m_list[i]]+subres;
            
def QPL2(m_l):
#
    temp=[]
    for j in QPL(m_l):
        tempp=list2num(j)
        if tempp not in temp:
            temp.append(tempp)
    return temp
    

#for i in QPL([1,2,3]):
#    print(i)

def zuhe(a,b):   #从a中选b个
    for i in list(itertools.permutations(a,b)):
        yield i
        

#因子个数,simple
def yinzi(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=1
    return sum
#连分数表示，精确度未知    
def continued_fractions( real, max_elements ):
	''' 
		takes a floating point number and returns it's continued fraction
		up to max_elements in the returned list, less than max_elements if a period is detected
	'''
	rest = real
	cf = []
	rests = {}
	is_periodic = False
	flag=0  
	while True:
		numerator = math.floor(rest) #获得整数
		rest -= numerator
		if numerator not in rests.keys():
			rests[numerator] = set([rest])
		else:
			found_same_rest = False
			for r in rests[numerator]:
				if math.fabs( (r - rest)/rest ) < 0.01 :
					# found the period
					found_same_rest = True
					is_periodic = True
					flag=rest
					#print('found repeated numerator: '+str(numerator))
					break
			if found_same_rest:
				break
		rests[numerator].add(rest)
		cf += [numerator]
		rest = 1/rest
		if len(cf) == max_elements:
			break
	return (cf, is_periodic, rests,flag)

#用chakravala方法解pell方程:x^2-N*y^2=1
#http://en.wikipedia.org/wiki/Chakravala_method#The_method    
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
        
    
