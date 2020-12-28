import time

#subtract 2 tuples
def subt(t1, t2):
    return(tuple(map(lambda i,j: i-j, t1, t2)))

#add 2 tuples
def addt(t1, t2):
    return(tuple(map(lambda i,j: i+j, t1, t2)))

def read_area(fname):
    with open(fname) as fp:
        m = [list(line.strip('\n')) for line in fp]

    return(m)

def write_area(fname, area):
    with open(fname, 'w') as fp:
        fp.write('\n'.join([''.join(row) for row in area]))

def read_shape(fname):
    a = read_area(fname)

    for y, row in enumerate(a):
        for x, c in enumerate(row):
            if c == 'X':
                ref = (y, x)

    return( [subt((y, x), ref) for y, row in enumerate(a) for x, c in enumerate(row) if c != ' '])

def valid_move(pos, shape, area, l, w):
    for p in shape:
        t = addt(p, pos)
        if min(t) < 0 or t[0] >= l or t[1] >= w or area[t[0]][t[1]] == 'x':
            return (False)
    return(True)


def clean(area, st_body, st_brush):
    l = len(area)

    for y, row in enumerate(area):
        w = len(row)
        for x, c in enumerate(row):
            if c != 'x' and valid_move((y,x), st_body, area, l, w):

                #do the cleaning
                for p in st_brush:
                    t = addt(p, (y, x))
                    if min(t) >= 0 and t[0] < l and t[1] < w and area[t[0]][t[1]] == ' ':
                        area[t[0]][t[1]] = '.'

def main():
    area = read_area('2020\\l17_kart.txt')
    w = [len(row) for row in area]
    print(max(w), min(w))

    st_body = read_shape('2020\\l17_st_body.txt')
    st_brush = read_shape('2020\\l17_st_brush.txt')

    clean(area, st_body, st_brush)

    write_area('2020\\l17_clean.txt', area)
    print(sum([1 for row in area for c in row if c == ' ']))


s=time.time()
main()
print (time.time()-s)

