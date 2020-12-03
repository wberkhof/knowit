import time

def isprime(num):
    if num > 1:
        # Iterate from 2 to n / 2  
        for i in range(2, num//2+1): 
                
            # If num is divisible by any number between  
            # 2 and n / 2, it is not prime  
            if (num % i) == 0: 
                return False
    else: 
        return False

    return True

def sumdigits(n): 
    sum = 0
    while (n != 0): 
        sum += n%10
        n = n//10
      
    return sum

def isharshadprime(num, primes):
    denom = sumdigits(num)

    #return num%denom == 0 and denom in primes
    return num%denom == 0 and isprime(denom)

def getharshadprimes(ulimit):
    primes=set([i for i in range(2, 9*len(str(ulimit))) if isprime(i)])

    assert isharshadprime(1729, primes)

    svar=0
    for i in range(1,ulimit):
        if isharshadprime(i, primes):
            svar+=1
    
    return svar

def main():
    s=time.time()
    print(getharshadprimes(98765432))
    print (time.time()-s)

    # l=[i for i in range(1,100)]
    # print(len([i for i in range(1000000) if sumdigits(i) in l]))

main()