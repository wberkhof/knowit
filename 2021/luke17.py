
import math

def roll(num):
    yield(num)
    s=str(num)

    for _ in range(len(s)-1):
        s=s[1:]+s[0]
        yield(int(s))

def main():
    svar=0
    triang=0
    for i in range(1_000_000):
        triang+=i
        
        for n in roll(triang):
            if math.sqrt(n).is_integer():
                #print(i, triang, n, math.sqrt(n))
                svar+=1
                break

    print(svar)


main()