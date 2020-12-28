import time

def read_patients(fname):
    with open(fname) as fp:
        p = [tuple(line.strip('\n').split(',')) + (n,) for n, line in enumerate(fp)] 

    return(p)

def treat(patients: list):
    prio = []
    treated = []

    for p in patients:
        if p[0] == '---':
            prio.sort(key=lambda tup: int(tup[1]) * 10000 + tup[2])
            treated.append(prio.pop(0))
        else:
            prio.append(p)
    
    prio.sort(key=lambda tup: int(tup[1]) * 10000 + tup[2])
    for p in prio:
        if p[0] == 'Claus':
            break
        else:
            treated.append(p)

    return(treated)


def main():
    patients = read_patients('2020\\l21_input.txt')
    treated = treat(patients)

    print(len(treated))


s=time.time()
main()
print (time.time()-s)