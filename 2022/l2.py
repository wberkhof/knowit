import math

def count_lines (gaver:list):
    lines = 0
    approved = 0

    for gave in gaver:
        lines += 2 + (approved-2 if approved>2 else 0)

        if gave.find('alv') < 0:
            approved += 1
    
    return(lines)

def main():
    with open('2022/l2_gaver.txt', 'r', encoding='utf-8') as dict_in:
        gaver = [line.rstrip('\n') for line in dict_in.readlines()]

    print (count_lines(gaver))

main()