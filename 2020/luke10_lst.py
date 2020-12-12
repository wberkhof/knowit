import time

def read_results(fname):
    with open(fname) as fp:
        m = [line[:-1].split(',') for line in fp]

    return(m)

def rank_alves(leker: list):
    d = { alv: 0 for l in leker for alv in l}

    for l in leker:
        for alv in l:
            d[alv] += len(l) - (l.index(alv)+1)

    return (dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))
    
def main():
    leker = read_results('2020\\l10_leker.txt')
    d = rank_alves(leker)

    alves = list(d)
    print('-'.join([alves[0], str(d[alves[0]])]))


s=time.time()
main()
print (time.time()-s)

