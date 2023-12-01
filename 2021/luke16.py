
def sailout(fjord, start):
    fjordlen=len(fjord[0])

    turns=0
    dir=-1
    y=start[1]

    for x in range(start[0]+1,fjordlen):
        if (y+3*dir)<0 or fjord[y+3*dir][x:x+1].count('#')>0:
            dir *= -1
            turns += 1
        else:
            y+=dir

        fjord[y][x] = '/' if dir==-1 else '\\'
    return(turns)

def main():
    fjord = list()

    for line in open("fjord.txt").readlines():
        l = list(line.strip('\n'))
        fjord.append(list(line))

        if l.count('B')>0:
            start=(l.index('B'), len(fjord)-1)

    print(sailout(fjord, start)+1)
    with open('fjord_sail.txt','w') as f:
        for l in fjord:
            f.writelines(''.join(l)+'\n')
        f.close()
        


main()