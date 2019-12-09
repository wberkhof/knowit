NUM_SPACE=27644437

for x in range(2, 25):
    for i in range(1, x):
        b=(NUM_SPACE*i)+1
        if b%x==0:
            y=int(b/x)
            z=y*5897
            print(x, z%NUM_SPACE, y)


def effeniet():
    for x in range(2, 25):
        for y in range(2, NUM_SPACE-1):
            b=y*x
            if b%NUM_SPACE==1:
                z=y*5897
                print(x, z%NUM_SPACE, y)
                break

