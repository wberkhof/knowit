from bases import Bases

def is_palindrome(s:str):
    return (1 if s == s[::-1] else 0)

def main():
    bases = Bases()

    result = 0
    for i in range(10000000):
        cnt = 0

        for base in range(2, 17):
            cnt += is_palindrome(bases.toBase(i, base))
            if cnt >= 3:
                result += i
                break

    print(result)


main()