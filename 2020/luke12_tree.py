import time

def read_family(fname):
    with open(fname) as fp:
        fam = fp.read().split(' ')

    return(fam)

def group_by_generation(fam: list):
    level = 0
    generations = []

    for n in fam:
        name = n.strip('(').strip(')')

        down = 1 if n.find('(') > -1 else 0
        up = len(n) - n.find(')') if n.find(')') > -1 else 0

        level += down
        if level > len(generations)-1:
            generations.append([])
        
        generations[level].append(name)
        level -= up

    return(generations)

    
def main():
    fam = read_family('2020\\l12_family.txt')

    #fam = 'Alvor (Alv Alf Alvaro (Halfrid Halvar Halvard (Alvilde Alva (Alfie Alvor Joralv) Alfonse)) Calvin (Tjalve Alvbert Alvard))'.split(' ')
    print(len(fam))

    generations = group_by_generation(fam)    

    print(max([len(names) for names in generations]))



s=time.time()
main()
print (time.time()-s)

