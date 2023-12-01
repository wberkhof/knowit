import png
import array as arr

PIX_BLACK=0
PIX_WHITE=255

def is_black(v: int):
    return(sum([int(b) for b in bin(v)[2:]]) % 2 == 0)

def draw_img(encrypted: list):
    h = len(encrypted)
    w = len(encrypted[0])

    graph=arr.array('B')
    graph.extend([PIX_WHITE] * h * w)

    for y in range(h):
        for x in range(w):
            if is_black(encrypted[y][x]):
                graph[(y * w) + x] = PIX_BLACK


    with open('2022/l7_image.png', 'wb') as fp:
        img = png.Writer(w, h, greyscale=True)
        img.write_array(fp, graph)


def main():
    #with open('2022/l7_encrypted_julestjerne.txt', 'r', encoding='utf-8') as fp:
    with open('2022/l7_encrypted.txt', 'r', encoding='utf-8') as fp:
        encrypted = [[int(d) for d in line.rstrip(' \n').split(' ')] for line in fp.readlines()]

    draw_img(encrypted)

main()