def main():
    votes = dict()

    with open('2022/l6_slemmehandlinger.txt', 'r', encoding='utf-8') as fp:
        vices = {line.split(':')[0]: float(line.split(':')[1].rstrip('\n')) for line in fp.readlines()}

    with open('2022/l6_stemmer.txt', 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            vote = line.split(':')[1].rstrip('\n') 
            weight = 1
            
            for v in line.split(':')[0].split(','):
                if v in vices and vices[v] < weight:
                    weight = vices[v]
            
            if vote not in votes:
                votes[vote] = weight
            else:
                votes[vote] += weight

    print(round(votes['julenissen']-votes['alvekongen']))

main()