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

def create_seq(n):
    seq = [0, 1]
    lookup = set(seq)

    for i in range(2, n):
        t = seq[i-2] - i

        t = t if t > 0 and t not in lookup else seq[i-2] + i
        seq.append(t)
        lookup.add(t)

    return(seq)

def main():
    seq = create_seq(1800813)
    primes = get_primes(max(seq))

    print(len([t for t in seq if t in primes]))

s=time.time()
main()
print (time.time()-s)
