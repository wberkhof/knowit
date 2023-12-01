from collections import deque

def cut_paper (pakker:list):
    length = 0

    for pak in pakker:
        p = deque(pak)

        best_margin = 110
        best_idx = -1

        for i in range(3):
            margin = 110
            if (p[0] + p[1]) <= 55:
                margin = 110 - 2 * (p[0] + p[1])
            elif (p[0] + p[1]) <= 110:
                margin = 110 - (p[0] + p[1])
            if margin < best_margin:
                best_margin = margin
                best_idx = i

            p.rotate(1)
        
        p.rotate(best_idx)
        if (p[0] + p[1]) <= 55:
            length += min(p[0], p[1]) + p[2]
        else:
            length += 2*(min(p[0], p[1]) + p[2])
       
    return(length)

def cut_paper2 (pakker:list):
    length = 0

    for p in pakker:
        if (p[0] + p[1]) <= 55:
            length += min(p[0], p[1]) + p[2]
        else:
            length += 2*(min(p[0], p[1]) + p[2])
       
    return(length)

def main():
    with open('2022/l3_pakker.csv', 'r', encoding='utf-8') as pakker_csv:
        pakker = [[int(d) for d in line.rstrip('\n').split(',')] for index, line in enumerate(pakker_csv.readlines()) if index > 0]

    paper = cut_paper2(pakker)
    #paper = cut_paper2([[30, 30, 20], [30, 30, 30], [25, 30, 20]])
    #paper = cut_paper2([[30, 25, 85]])
    print (paper)

#2b+2h -> l+h
#2l+2b -> h+b
#2h+2l -> b+l


main()