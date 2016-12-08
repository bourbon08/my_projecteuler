import primesieve
import math
 
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#
def pan(n):   
    if n%10 not in [3,5,7]: 
        return False
    m=n
    for i in range(1,len(str(n))+1):
        if not isPrime(n%(10**i)):
            return False     
        if not isPrime(m):
            return False
        m=int(m/10)
    return True            
               
if __name__ == "__main__":
    it = primesieve.Iterator()
    it.skipto(12)
    prime = it.next_prime()

    count=0
    sum=0

    while count!=11:
        if pan(prime):
            print(prime)
            sum+=prime
            count+=1
        prime = it.next_prime()
        ll.append(prime)
            
            
    print(sum)
       