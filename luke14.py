import array as arr

SEQ_SZ=217532235
#SEQ_SZ=20
TEST_NUM=7


def main():
    svar = 0
    seq = arr.array('B')

    alfa = [2,3,5,7,11]

    i_read = 1
    i_write = alfa[0]
    i_alfa = 1
    seq.extend([alfa[0]] * alfa[0])

    while i_write < SEQ_SZ:
        seq.extend([alfa[i_alfa]] * seq[i_read])

        i_write += seq[i_read]
        i_read += 1
        i_alfa = 0 if i_alfa == len(alfa)-1 else i_alfa+1

    print(seq.count(7)*7)





main()