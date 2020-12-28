import time
import csv

def read_wordlist(fname):
    with open(fname, encoding='utf-8') as fp:
        wl = {line.strip() for line in fp}
    
    return (wl)

def read_pairs(fname):
    with open(fname, encoding='utf-8') as fp:
        pairs = [[p.strip() for p in pair] for pair in csv.reader(fp, delimiter=',')]
    
    return (pairs)

def find_limords(pairs: list, wl: set):
    limords = set()

    for pair in pairs:
        lw = pair[0]
        l = len(lw)
        set_l = {w[l:] for w in wl if w[:l] == lw and w[l:] in wl}

        rw = pair[1]
        r = len(rw)
        limords = limords | {w[:-r] for w in wl if w[-r:] == rw and w[:-r] in set_l}

    return (limords)

def main():
    wl = read_wordlist('2020\\l15_wordlist.txt')
    pairs = read_pairs('2020\\l15_riddles.txt')

    limords = find_limords(pairs, wl)

    print(limords, len([c for w in limords for c in w]))

s=time.time()
main()
print (time.time()-s)
