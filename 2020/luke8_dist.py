
def manhattan_distance(p1, p2):
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))

def travel_duration(p_ref, p_dest):
    d = manhattan_distance(p_ref, p_dest)

    if d == 0:
        return(0)
    elif d < 5:
        return(0.25)
    elif d < 20:
        return(0.5)
    elif d < 50:
        return(0.75)
    else:
        return(1)
    
def read_places(fname):
    geo = {'route': [], 'positions': dict()}
    with open(fname, encoding='utf-8') as fp:
        for line in fp:
            l = line[:-1].split(':')

            if len(l) == 2:
                pos = l[1].strip(' ()').split(',')
                geo['positions'][l[0]] = [int(pos[0]), int(pos[1])]
            else:
                geo['route'].append(l[0])
    return(geo)

def travel(route: list, positions: dict):
    durations = {name: 0 for name, pos in positions.items()}

    start = [0,0]
    for name in route:
        dest = positions[name]

        step = -1 if start[0] > dest[0] else 1

        for x in range(start[0], dest[0], step):
            for place, pos in positions.items():
                durations[place] += travel_duration(pos, [x, start[1]])

        step = -1 if start[1] > dest[1] else 1

        for y in range(start[1], dest[1], step):
            for place, pos in positions.items():
                durations[place] += travel_duration(pos, [dest[0], y])

        start = list(dest)

    return(durations)

def main():
    geo = read_places('2020\\l8_route.txt')
    durations = travel(geo['route'], geo['positions'])

    print(durations)
    l = [t for name, t in durations.items()]
    print(max(l) - min(l))

    

main()