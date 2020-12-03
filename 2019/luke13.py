import json
import png
import array as arr
import sys

CELL_SZ=5
PIX_BLACK=0
PIX_WHITE=255
PIX_GRAY=125
XY_MOVE={'syd': (0,1,'nord'), 'aust': (1,0,'vest'), 'vest': (-1,0,'aust'), 'nord': (0,-1,'syd')}

class Step:
    def __init__(self, cell, strategy):
        self.x = cell['x']
        self.y = cell['y']
        self.directions = [dir for dir in reversed(strategy) if not cell[dir]]
        self.strategy = strategy
        self.path=False

    def __eq__(self, other):
        if type(other) is Step:
            return self.x == other.x and self.y == other.y
        else:
            return False

    def popnext(self, maze, trace):
        while len(self.directions)>0:
            dir = self.directions.pop()
            x = self.x + XY_MOVE[dir][0]
            y = self.y + XY_MOVE[dir][1]

            if trace[x][y] == None:
                step = Step(maze[y][x], self.strategy)
                trace[x][y] = step
                return step
        return self
    
    def __str__(self):
        return str((self.x, self.y)) + str(self.directions)

    def __repr__(self):
        return str((self.x, self.y)) + str(self.directions)

def draw_maze(maze, trace, fname):
    h=len(maze) * CELL_SZ + 1
    w=len(maze[0]) * CELL_SZ + 1

    graph=arr.array('B')
    graph.extend([PIX_WHITE] * h * w)

    for row in maze:
        for cell in row:
            draw_cell(cell, trace, graph, w)

    f = open(fname, 'wb')
    w = png.Writer(w, h, greyscale=True)
    w.write_array(f, graph)
    f.close()

def draw_cell(cell, trace, graph, w):
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
    
    s = trace[cell['x']][cell['y']]
    if type(s) is Step and s.path:
        for i in range(1,5):
            graph[start+(i*w)+1]=PIX_GRAY
            graph[start+(i*w)+2]=PIX_GRAY
            graph[start+(i*w)+3]=PIX_GRAY
            graph[start+(i*w)+4]=PIX_GRAY

def find_path(maze, strategy):
    max_x=len(maze)-1
    max_y=len(maze[0])-1
    trace=[[None for y in range(max_y+1)] for x in range(max_x+1)]  #init 2 dim array to keep track of visited cells

    step=Step(maze[0][0], strategy)
    trace[0][0]=step
    stack=[]
    tries=0

    try:
        while step.x != max_x or step.y != max_y:
            tries+=1
            next = step.popnext(maze, trace)
            if next != step:    #found next cell?
                stack.append(step)
                step = next
            else:
                step = stack.pop()
            
            if tries%10000 == 0:
                print(tries)
    
    except Exception as e:
        print('Failed to find path:', e, step.x, step.y)

    for s in stack:
        trace[s.x][s.y].path=True

    return trace

def main():
    with open('maze.txt') as f:
        maze = json.load(f)
        f.close()

    #trace = find_path(maze, ('aust', 'syd', 'vest', 'nord'))

    trace = find_path(maze, ('syd', 'aust', 'vest', 'nord'))
    print(len([c for row in trace for c in row if not c==None]))

    draw_maze(maze, trace, 'maze.png')

main()