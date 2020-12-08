import time

def get_primes(n):
    noprimes = set()
    primes = set()

    for p in range(2, n):
        if not p in noprimes:
            primes.add(p)
            for np in range(p**2, n, p):
                noprimes.add(np)
    return primes

def get_delivered(primes, n):
    delivered = []
    next_p = -1
    for p in range(0, n):
        if p > next_p:
            if '7' in str(p):
                next_p = p + min(primes, key=lambda x:abs(x-p))
            else:
                delivered.append(p)

    return delivered


s=time.time()

population = 5433000
#population = 10000

primes = get_primes(population)        
print(len(primes))
delivered = get_delivered(primes, population)

print(delivered, len(delivered))

print (time.time()-s)