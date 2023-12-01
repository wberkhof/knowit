from yaml import load


def main():
    with open('2023/l1_goals.txt', 'r', encoding='utf-8') as goals:
        line = goals.readline()
        g = list(map(int, line.rstrip('\n').split(',')))

    with open('2023/l1_bets.txt', 'r', encoding='utf-8') as bets:
        b = load(bets)

    print (g)
    print (b)

main()