import time

def read_wordlist(fname):
    with open(fname, encoding='utf-8') as fp:
        wl = [line.strip() for line in fp]
    
    return (wl)

def find_palinestendrom(wl: list):
    plntd = []

    for w in wl:
        if len(w)>3 and w != w[::-1]:    #check real palindrome
            is_palinestendrom = False
            i=0
            while i <= (len(w)-2)//2:
                r = -i-1    #reverse index
                if w[i] != w[r]:
                    if w[i:i+2] == w[r-1:r+1 if r<-1 else None]:
                        is_palinestendrom = True
                        i += 1
                    else:
                        is_palinestendrom = False
                        break
                i += 1

            if is_palinestendrom:
                plntd.append(w)
            
    print(plntd)

    return(plntd)

def main():
    wl = read_wordlist('2020\\l18_wordlist.txt')

    plntd = find_palinestendrom(['stylist','gnisning','kauka','baluba', 'tarotkorta'])
    print(len(plntd))

    plntd = find_palinestendrom(wl)
    print(len(plntd))

s=time.time()
main()
print (time.time()-s)
