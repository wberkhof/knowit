def calc_area(poles: list):
    x_min = min([p[0] for p in poles])
    x_max = max([p[0] for p in poles])
    
    #sort by y
    poles.sort(key=lambda p: p[1])

    x_bottom = poles[0][0]
    x_top = poles[len(poles)-1][0]
    gjerde = []

    backup = False

    lx = x_max

    for (x,y) in poles:
        if (not backup and x < lx) or (backup and x > lx and x <= x_top):
            gjerde.append((x,y))
            lx = x

        if x == x_min:
            backup = True

    backup = False

    for (x,y) in sorted(poles, key=lambda p: p[1], reverse=True):
        if (not backup and x > lx) or (backup and x < lx and x >= x_bottom):
            gjerde.append((x,y))
            lx = x

        if x == x_max:
            backup = True

    area = 0

    for i, (x1,y1) in enumerate(gjerde):
        if i==0:
            x2, y2 = gjerde[len(gjerde)-1]
        else: 
            x2, y2 = gjerde[i-1]

        area += (x1 * y2) - (y1 * x2)     
    
    print(area/2)
    print(len(poles), len(gjerde))
    print(gjerde)


def main():
    with open('2022/l8_data.txt', 'r', encoding='utf-8') as fp:
        poles = [(int(line.split(' ')[0]), int(line.split(' ')[1].strip('\n'))) for line in fp.readlines()]

    calc_area(poles)

#172464027278.5
#541092978158.0
#202602236535.0
#202602236535.0

main()