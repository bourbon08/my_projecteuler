import time  
import math  
def square_(x,epsilon):#二分法  
    assert x>=0  
    assert epsilon>0  
    low  = 0  
    high =max(x,1.0)  
    quess = (low+high)/2.0  
    ctr=1  
    while abs(quess**2-x)>epsilon and ctr<=100 :  
        if quess**2<x:  
            low = quess  
        else:  
            high = quess  
        quess = (low+high)/2.0  
        ctr+=1  
    assert ctr<=100  
    print(ctr) 
    return quess  
  
      
      
def squareNR(x,epsilon):   #牛顿法  
    assert x>=0  
    assert epsilon>0  
    x=float(x)  
    quess=x/2.0  
    quess=0.001  
    diff=quess**2-x  
    ctr=1  
    while abs(diff)>epsilon and ctr<=1000:  
        quess = quess-diff/(2.0*quess)  
        diff = quess**2-x  
        ctr +=1  
    print(ctr)  
    assert ctr<=100  
    return quess  
  
#测试代码  
s=squareNR(64535,0.0001)  
  
print(s)
  
  
  
s=math.sqrt(64535)  
print(s)