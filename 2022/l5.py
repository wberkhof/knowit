from bases import Bases

def shuffle_to_start(start:list):
    cnt = 0
    stokk = start

    while True:
        cnt += 1
        stokk = [n for i in zip(stokk[:len(stokk)//2],stokk[len(stokk)//2:]) for n in i]

        if cnt == 13:
            print (len(start), cnt)
            return (cnt if stokk == start else 0)


def main():
    cards=4

    while True:
        stokk = [i for i in range(1,cards+1)]

        if shuffle_to_start(stokk) == 13:
            print (cards)
            break

        cards += 2

main()