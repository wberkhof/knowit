import time

def read_leveringsliste(fname):
    d = {'sukker': 0, 'mel': 0, 'egg': 0, 'melk': 0}

    with open(fname) as fp:
        orders = ','.join([line.strip() for line in fp]).split(',')
    
    for order in orders:
        prod = order.split(':')[0].strip()
        qty = int(order.split(':')[1].strip())

        d[prod] += qty

    return(d)


s=time.time()

d = read_leveringsliste('2020\\l4_leveringsliste.txt')
print(d)
print(min([d['sukker']//2, d['mel']//3, d['melk']//3, d['egg']]))

print (time.time()-s)