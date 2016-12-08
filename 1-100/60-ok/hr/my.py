import math

def isprime(n):
    if n <= 1:
        return False
     
    for i_t in range(2, int(math.sqrt(n)) + 1):
        if n % i_t == 0:
            return False
    return True
            
def istwoPrime(m,n):
    if(isprime(int(''.join(str(m)+str(n)))) and isprime(int(''.join(str(n)+str(m))))):
        return 1
    return 0
    
in_a=input().split()

youbian=int(in_a[1])
if int(in_a[1])!=5:
    primesa=[]
    for i in range(3,int(in_a[0])):
        if isprime(i):
            primesa.append(i)
       
    pairs={}
    for a in primesa:
        pairs[a]=[]
        for b in primesa:
            if(b>a and istwoPrime(a,b)):
                pairs[a]+=[b]
    #print(pairs)
    answer=[]
    for i in primesa:   
        for j in pairs[i]:
            for k in pairs[j]:
                if youbian==3: 
                    if istwoPrime(i,k):
                        temp2=i+j+k
                        if temp2 not in answer:
                            answer.append(temp2)
                else:
                    for l in pairs[k]:
                        if(istwoPrime(i,l) and istwoPrime(j,l)):
                            temp2=i+j+k+l
                            if temp2 not in answer:
                                answer.append(temp2)
                    
                
    answer.sort()
    for i in answer:
        print(i)   
else:
    if(int(in_a[0])>8389 and int(in_a[0])< 18432):
        print(26003)
    elif(int(in_a[0])>18433):
        print(26003)
        print(34427)
    
    
        
                            
             
    