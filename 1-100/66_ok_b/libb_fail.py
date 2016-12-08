from decimal import Decimal as D
import math
import random

def gcd(a,b):
    while 1:
        r=a%b
        if not r:
            return b
        a=b
        b=r


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

def expand_cf( cf, periods ):
	''' given a continued fractions list, return the associated float '''
	if not cf:
		return None
	result = 0.0
	previous_inverse = 0.0
	if not periods:
		periods = 1
	for i in range(periods):
		for a in reversed(cf[1:]):
			previous_inverse = 1/(a+previous_inverse)
	previous_inverse = 1/(cf[0]+previous_inverse)
	return 1/previous_inverse
		

def prng(max_iter):
	count = 0
	while count < max_iter:
		yield random.randint(0, 256)
		count += 1


def returnx(i):
    a = continued_fractions(D(math.sqrt(D(i))), 200000)
    b = continued_fractions(D(a[3]),200)[0]
    cf=a[0];zhouqi=len(b)-1
    p=1;q=cf[-2]
    for j in range(3,len(cf)):
        p=cf[-j]*q+p
        temp=q
        q=p
        p=temp
    if len(a[0])-zhouqi!=1:
        print(len(a[0])-zhouqi,i)
    
    p=cf[0]*q+p
    temp=gcd(p,q)
    p=int(p/temp)
    q=(q/temp)
    if p*p-i*q*q==1:
        return (p,q)
    else:
        return (p*p+i*q*q,2*p*q)
    


if __name__ == "__main__":
    #example
    cf = continued_fractions(math.sqrt(73), 20)
    print('sqrt(2)=' + str(cf[0]) )
    print( expand_cf(cf[0], 10))

    max_i=0
    max_x=0
    ll=[]
    for i in range(2,33):
        ll.append(i*i)


    for i in range(10,1001):
        if i in ll:
            continue
        x=returnx(i)[0]
        if x>max_x:
            max_x=x
            max_i=i

    print(max_i)       