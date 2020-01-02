import png
import array as arr

PIX_BLACK=0
PIX_WHITE=255
CWDTH=400
CHGTH=400

def drawtrips(trips, fname):
    h = CHGTH
    w = CWDTH * len(trips)

    graph=arr.array('B')
    graph.extend([PIX_WHITE] * h * w)

    i = 0
    for trip in trips:
        drawtrip(graph, trip, i, w)
        i += 1

    f = open(fname, 'wb')
    w = png.Writer(w, h, greyscale=True)
    w.write_array(f, graph)
    f.close()

def drawtrip(graph, trip, offset, w):
    for c in trip:
        x = int(c[0])
        y = CHGTH - int(c[1])
        i = (y * w) + (x + offset * CWDTH)
        graph[i]=PIX_BLACK

def readtrips(fname):
    trips = list()
    trip = list()

    for line in open(fname).readlines():
        line=line.strip('\n')

        if line == '---':
            trips.append(trip)
            trip = list()
        else:
            trip.append(line.split(','))
    
    trips.append(trip)

    return trips

def main():
    trips = readtrips('turer.txt')

    print(len(trips))

    for t in trips:
        print(max([int(c[0]) for c in t]), max([int(c[1]) for c in t]))

    drawtrips(trips, 'turer.png')

main()