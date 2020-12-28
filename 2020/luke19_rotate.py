import time
from collections import deque

def read_games(fname):
    l = []

    with open(fname) as fp:
        for line in fp:
            a = line.strip(']\n').split('[')

            game = {}
            game['rule'] = int(a[0].split(' ')[0])
            game['shift'] = int(a[0].split(' ')[1])
            game['alves'] = a[1].split(', ')

            l.append(game)

    return(l)


def play(games: list):
    for game in games:
        alves = deque(game['alves'])
        i = 0
        while len(alves) > 1:
            alves.rotate(game['shift'])

            if game['rule'] == 1:
                del alves[0]
            elif game['rule'] == 2:
                del alves[i]
                i = i+1 if i < len(alves)-1 else 0
            elif game['rule'] == 3:
                c = len(alves) // 2 if len(alves) > 2 else 0
                if len(alves) % 2 == 0 and c > 1:
                    del alves[c-1]
                    del alves[c]
                else:
                    del alves[c]
            else:
                del alves[-1]
        game['winner'] = alves[0]


def main():
    games = read_games('2020\\l19_input.txt')

    play(games)
    
    winners = [game['winner'] for game in games]
    #print(winners)
    print(max(winners, key = winners.count))

s=time.time()
main()
print (time.time()-s)

