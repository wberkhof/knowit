
def read_matrix(fname):
    with open(fname, encoding='utf-8') as fp:
        lines = [line.strip() for line in fp]
    
    max_y = len(lines)
    max_x = len(lines[0])

    v = d1 = d2 = str()
    xd = yd = 0

    for i in range(0, max_x * max_y):
        yv = i % max_y
        xv = i // max_x

        v += lines[yv][xv]
        d1 += lines[yd][xd]
        d2 += lines[yd][max_x-xd-1]

        if yd == max_y-1:
            yd = xd + 1
            xd = max_x-1
        elif xd == 0:
            xd = yd + 1
            yd = 0
        else:
            xd -= 1
            yd += 1

    d = dict()
    d['h'] = str().join(lines)
    d['hr'] = str().join([rl[::-1] for rl in reversed(lines)])
    d['v'] = v
    d['vr'] = str().join(reversed(v))
    d['d1'] = d1
    d['d1r'] = str().join(reversed(d1))
    d['d2'] = d2
    d['d2r'] = str().join(reversed(d2))

    return (d)

def find_words(d: dict, words: set):
    found = set()
    for i, txt in d.items():
        print('search:', i)
        for word in words:
            if word in txt:
                found.add(word)
                print(i, word)
    
    return (found)

d = read_matrix('2020\\luke3_matrix.txt')

with open('2020\\luke3_wordlist.txt', encoding='utf-8') as fp:
    words = set([line.strip() for line in fp])

not_found = list(words - find_words(d, words))


print(",".join(sorted(not_found)))
