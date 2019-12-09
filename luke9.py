
def krampus(n):
    sq = n**2

    for x in range(2, len(str(sq))):
        div=10**x

        if sq%div != 0 and sq//div + sq%div == n:
            print(n, sq, div, sq//div, sq%div)
            return n
    
    return 0

def main():
    sum = 0

    for line in open("krampus.txt").readlines():
        sum = sum + krampus(int(line))

    print(sum)

main()