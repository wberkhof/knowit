import json
import png
import array as arr
import sys

CELL_SZ=5
PIX_BLACK=0
PIX_WHITE=255
XY_MOVE={'syd': (0,1,'nord'), 'aust': (1,0,'vest'), 'vest': (-1,0,'aust'), 'nord': (0,-1,'syd')}

def draw_maze(maze, fname):
    h=len(maze) * CELL_SZ + 1
    w=len(maze[0]) * CELL_SZ + 1

    graph=arr.array('B')
    graph.extend([PIX_WHITE] * h * w)

    for row in maze:
        for cell in row:
            draw_cell(cell, graph, w)

    f = open(fname, 'wb')
    w = png.Writer(w, h, greyscale=True)
    w.write_array(f, graph)
    f.close()

def draw_cell(cell, graph, w):
    start=cell['y']*w*5 + cell['x']*CELL_SZ

    for i in range(5):
        if cell['nord']:
            graph[start+i]=PIX_BLACK
        if cell['vest']:
            graph[start+i*w]=PIX_BLACK
        if cell['syd']:
            graph[start+5*w+i]=PIX_BLACK
        if cell['aust']:
            graph[start+i*w+5]=PIX_BLACK

def find_path(maze, strategy, x, y, from_dir):
    cell=maze[y][x]

    if x==499 and y==499:
        return True

    if 'visited' not in cell:
        print(x,y)
        cell['visited'] = True

        for dir in strategy:
            if not cell[dir] and find_path(maze, strategy, x+XY_MOVE[dir][0], y+XY_MOVE[dir][1], XY_MOVE[dir][2]):
                cell['path'] = from_dir
                return True
    
    return False

def main():
    sys.setrecursionlimit(800*800)

    with open('maze.txt') as f:
        maze = json.load(f)
        f.close()

    trace=[[dict(c) for c in row] for row in maze]
    
    if find_path(trace, ('aust', 'syd', 'vest', 'nord'), 0, 0, None):
#    if find_path(trace, ('syd', 'aust', 'vest', 'nord'), 0, 0, None):
        print('path', len([c for row in trace for c in row if 'path' in c]))  #flatten maze

    print('visited', len([c for row in trace for c in row if 'visited' in c]))  #flatten maze

    trace=[[dict(c) for c in row] for row in maze]
    
    if find_path(trace, ('aust', 'syd', 'vest', 'nord'), 0, 0, None):
        print('path', len([c for row in trace for c in row if 'path' in c]))  #flatten maze

    print('visited', len([c for row in trace for c in row if 'visited' in c]))  #flatten maze

    #draw_maze(maze, 'maze.png')

main()