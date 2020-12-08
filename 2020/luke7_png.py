import png
import array as arr

PIX_BLACK=0
PIX_WHITE=255


def draw_png(lines, fname):
    h = len(lines)
    w = max([len(line) for line in lines])

    graph=arr.array('B')
    graph.extend([PIX_BLACK] * h * w)

    for y in range(h):
        line = lines[y]
        for x in range(w):
            if len(line) > x and line[x]=='#':
                graph[(y*w)+x]=PIX_WHITE

    with open(fname, 'wb') as fp:
        w = png.Writer(w, h, greyscale=True)
        w.write_array(fp, graph)


def read_forest(fname):
    with open(fname) as fp:
        lines = [line[:-1] for line in fp]

    return(lines)

def check_trees(forest):
    truncs = [i for i in range(len(forest[-1])) if forest[-1][i] == '#']
    print(len(truncs))

    symmetriske = 0
    for i in truncs:
        for y in forest:
            x = 0
            while y[i+x] == y[i-x] and (y[i+x] == '#' or y[i+x+1] == '#'):
                x += 1

            if y[i+x] != y[i-x]:
                break

        if y == forest[-1]:
            symmetriske += 1

    return(symmetriske)
            
            


def main():
    forest = read_forest('2020\\l7_forest.txt')
    draw_png(forest, '2020\\l7_forest.png')

    print(check_trees(forest))
main()