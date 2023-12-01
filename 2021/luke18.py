#    sum1 = sum([string.ascii_lowercase.index(x.lower()) + 1 for x in part1 if x.lower() in string.ascii_lowercase]) 

import numpy as np
import re
from math import ceil

def i_ext(fname, lname, gen):
    slice = ceil(len(lname)/2)
    if gen=='M':
        return np.prod(np.array([ord(c) for c in lname[slice:]], dtype=np.int64)) * len(fname)
    else:
        return np.prod(np.array([ord(c) for c in lname[slice:]], dtype=np.int64)) * len(fname+lname)

def i_fn(fname):
    return sum([ord(c) for c in fname])

def i_ln(lname):
    slice = ceil(len(lname)/2)
    return sum([ord(c)-ord('a')+1 for c in lname[:slice].lower()])

def rsort(num):
    return int(''.join(sorted(str(num), reverse=True)))


def main():
    az = re.compile("[^a-zA-Z,]")
    emp = [az.sub('',line).split(',') for line in open("employees.csv").readlines()]

    #emp = ['Onfre,Hatley,M'.split(',')]
    names = [line.strip('\n') for line in open("names.txt").readlines()]
    fn = {'M': names[:36], 'F': names[37:67]}
    ln = names[68:92]
    ext = names[93:]

    #out = [e + [fn[e[2]][i_fn(e[0])%len(fn[e[2]])] + ' ' + ln[i_ln(e[1])%len(ln)] + ext[rsort(i_ext(e[0], e[1], e[2]))%len(ext)]] for e in emp[1:]]
    out = [fn[e[2]][i_fn(e[0])%len(fn[e[2]])] + ' ' + ln[i_ln(e[1])%len(ln)] + ext[rsort(i_ext(e[0], e[1], e[2]))%len(ext)] for e in emp[1:]]

    # with open('nameswb.txt','w') as f:
    #     for l in out:
    #         f.writelines(','.join(l)+'\n')
    #     f.close()

    svar = sorted([(e, out.count(e)) for e in np.unique(out)], key=lambda x: x[1])
    #print('Johannsen', rsort(i_ext('Jan', 'Johannsen'))%26, ext[rsort(i_ext('Jan', 'Johannsen'))%26])
    #print(emp[1][1])
    #print(ext[0])
    print(svar)

main()