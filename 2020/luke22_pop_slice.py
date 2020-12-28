import time

def read_lines(fname):
    l = []

    with open(fname) as fp:
        for line in fp:
            a = line.strip(']\n').split(' [')

            line = {}
            line['text'] = list(a[0])
            line['names'] = a[1].lower().split(', ')

            l.append(line)

    return(l)

def validate_words(lines: list):
    for line in lines:
        text = line['text']
        names = line['names']
        valid = []

        for name in names:
            s = []
            t = list(text)  #backup last state
            p = 0

            for c in name:
                if c in text[p:]:
                    p = text.index(c, p)
                    s.append(text.pop(p))
                else:
                    break

            if name == ''.join(s):
                valid.append(name)
            else:
                text = t    #revert to last state

        line['valid'] = valid

    v = [len(line['valid']) for line in lines]
    print(v.index(max(v)))


def main():
    lines = read_lines('2020\\l22_input.txt')

    #lines = [{'text': list('llmnmgimnaaiechhchajghefgjkudri'), 'words': ['michael', 'guri', 'aksel']}]
    validate_words(lines)
    

s=time.time()
main()
print (time.time()-s)
