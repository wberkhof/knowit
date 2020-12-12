import time

def read_matrix(fname):
    with open(fname) as fp:
        m = [list(line[:-1]) for line in fp]

    return(m)

def spread_virus(m: list):
    MAX_Y = len(m)
    MAX_X = len(m[0])

    trace = []
    
    while True:
        infections = 0
        next = []
        for y in range(MAX_Y):
            next.append(list(m[y])) #copy for next round

            f = (x for x in range(MAX_X) if m[y][x] == 'F')
            for x in f:
                contacts = 0
                for ny in range(y-1, y+2, 2):
                    if 0 <= ny < MAX_Y and m[ny][x]=='S':
                        contacts += 1
                for nx in range(x-1, x+2, 2):
                    if 0 <= nx < MAX_X and m[y][nx]=='S':
                        contacts += 1
                        
                #l1 = [ny for ny in range(y-1, y+1, 2) if 0 <= ny <= MAX_Y and m[ny][x]=='S']
                #l2 = [nx for nx in range(x-1, x+1, 2) if 0 <= nx <= MAX_X and m[y][nx]=='S']

                if contacts >= 2:
                    next[y][x] = 'S'
                    infections += 1

        trace.append(m)
        m = next
        
        if infections > 0:
            print(len(trace), infections)
        else:
            total_infected = len([c for l in m for c in l if c=='S'])
            print(total_infected)
            break

    return(len(trace))

def main():
    m = read_matrix('2020\\l9_elves.txt')
    print(spread_virus(m))


s=time.time()
main()
print (time.time()-s)

