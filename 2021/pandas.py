#!/usr/bin/env python3

import sys
import re
import datetime
import pandas

year = 2018
sizes = {
    'tannkrem': 125,
    'sjampo': 300,
    'toalettpapir': 25,
}

pk = re.compile(r'^(\w+\s\d+):$')
pv = re.compile(r'^\s\*\s(\d+)\s(\w+)\s(\w+)$')

data = []
cur = None
for line in sys.stdin.readlines():
    if m := pk.match(line):
        cur = m.group(1)
    elif m := pv.match(line):
        data.append({
            'date': datetime.datetime.strptime(f'{cur} {year}', '%b %d %Y'),
            'item': m.group(3),
            'amount': int(m.group(1)),
            'unit': m.group(2),
        })
    else:
        raise Exception(f'could not parse line: {line}')

df = pandas.DataFrame.from_records(data, index='date')

# antall hele tuber tannkrem brukt i 2018
tubes = df[df['item'] == 'tannkrem']['amount'].sum() // sizes['tannkrem']
# antall hele flasker sjampo brukt i 2018
bottles = df[df['item'] == 'sjampo']['amount'].sum() // sizes['sjampo']
# antall hele toalettruller brukt i 2018
rolls = df[df['item'] == 'toalettpapir']['amount'].sum() // sizes['toalettpapir']
# antall milliliter sjampo brukt på søndager
sunpoo = df[(df['item'] == 'sjampo') & (df.index.dayofweek == 6)]['amount'].sum()
# antall meter toalettpapir brukt på onsdager
sunpaper = df[(df['item'] == 'toalettpapir') & (df.index.dayofweek == 2)]['amount'].sum()

print(tubes * bottles * rolls * sunpoo * sunpaper)