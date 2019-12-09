#proxypip install pypng
#https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python

import png
import array as arr

def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

reader = png.Reader(filename='mush.png')

w, h, mush, meta = reader.read_flat()

#mush = [240, 33, 11, 61, 78, 109, 69, 46, 106, 104, 45, 160, 36, 192, 143]
cnt=0
out=arr.array('B')
_rgb=[0,0,0]

for rgb in grouped(mush, 3):
    pix = [byte ^ _rgb[i] for i,byte in enumerate(rgb) ]
    out.extend(pix)
    _rgb=rgb
    cnt = cnt + 1

print(w, h, cnt)

f = open('swatch.png', 'wb')
w = png.Writer(w, h, greyscale=False)
w.write_array(f, out)
f.close()
