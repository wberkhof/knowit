
class sint(int):
    def reverse(self):
        return sint(str(self)[::-1])
    
    def sortdigits(self, digits):
        return sint(''.join(sorted(str(self).zfill(digits), reverse=True)))

svar=0

for t in range(1000, 10000):
    t1 = sint(t).sortdigits(4)
    t2 = t1.reverse()
    
    if t1 != t2:
        for i in range(1, 8):
            if t1 > t2:
                diff = t1 - t2
            else:
                diff = t2 - t1

            if diff==6174:
                if i==7:
                    svar+=1
                    #print(t, i)
                break
            else:
                t1= sint(diff).sortdigits(4)
                t2 = t1.reverse()

        if i>7:
            print(t, i)

print(svar)

def f(x):
    if not x or x == 6174:
        return 0
    a = int("".join(sorted(f"{x:04}", reverse=True)))
    b = int("".join(sorted(f"{x:04}", reverse=False)))
    
    return f(a-b)+1


[ f(i) for i in range(1000,10000)].count(7)