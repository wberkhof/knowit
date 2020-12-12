import time
import numpy


def read_hints(fname):
    with open(fname) as fp:
        hints = [line[:-1] for line in fp]

    return(hints)

def _ord(c):
    return (ord(c)-97)

def _chr(n):
    return (chr(n+97))

def _add(c1, c2):
    return(_chr((_ord(c1) + _ord(c2))%26))

def _shr(c):
    return(_chr((_ord(c) + 1)%26))

def encode(txt: str):
    return ''.join([_add(txt[i], _shr(txt[i+1])) for i in range(len(txt)-1)])

def parse_hint(hint: str):
    txt = hint
    l = [txt]

    while len(txt) > 1:
        txt = encode(txt)
        l.append(txt)

    codes = [''.join([l[y][x] for y in range(len(l)-x)]) for x in range(len(hint)) ]
    
    for txt in codes:
        if txt.find('eamqia') > -1:
            print(hint)

def parse_hints(hints: list):
    #d = { hint: [] for hint in hints}

    for hint in hints:
        parse_hint(hint)



    
def main():
    hints = read_hints('2020\\l11_hint.txt')
    parse_hints(hints)
    print(len(hints))
    #print('-'.join([alves[0], str(d[alves[0]])]))


s=time.time()
main()
print (time.time()-s)

