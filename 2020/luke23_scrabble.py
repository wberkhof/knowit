import time

def read_wordval(fname):
    with open(fname, encoding='utf-8') as fp:
        wv = {l[0]: int(l[1]) for l in [line.strip('\n').split(' ') for line in fp]}

    return(wv)

def read_battles(fname):
    with open(fname, encoding='utf-8') as fp:
        bt = [(l[0], l[1].split(' ')) for l in [line.strip('\n').split(': ') for line in fp]]

    return(bt)

def compete(bt, wv):
    vocals = 'aeiouyæøå'
    score = {nm: 0 for (nm, rap) in bt}

    for (nm, rap) in bt:
        last_base = ''
        points = 0
        vc = last_vc = 0
        rep = 1

        for word in rap:
            base = word[4:] if word[:4] == 'jule' else word
            jb = 2 if word[:4] == 'jule' else 1
            
            vc = len([c for c in word if c in vocals])  
            vb = (vc-last_vc)*jb if last_vc>0 and (vc-last_vc)>0 else 0
            last_vc = vc

            if base == last_base:
                rep += 1
            else:
                rep = 1
            last_base = base

            points += (wv[base]+vb) // rep
        
        score[nm] += points

    return (score)



def main():
    wv = read_wordval('2020\\l23_basewords.txt')
    bt = read_battles('2020\\l23_rap_battle.txt')

    score = compete(bt, wv)

    print(score)

s=time.time()
main()
print (time.time()-s)