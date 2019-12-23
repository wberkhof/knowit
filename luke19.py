
def ispalindrome(n):
    return (n == reversenum(n))

def ishiddenpalindrome(n):
    return ispalindrome(n + reversenum(n))

def reversenum(n):
    return int(str(n)[::-1])

def main():
    #svar = sum([i for i in range(1, 123454321) if ishiddenpalindrome(i)])
    svar=0
    for i in range(1, 123454321):
        if not ispalindrome(i) and ishiddenpalindrome(i):
            svar+=i
    print(svar)

main()