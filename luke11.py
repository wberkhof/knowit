
brake_factor_km = \
{
    'G':27,
    'I':-12,
    'A':59,
    'S':212,
    'F':70
}

terrain = open("terreng.txt").read()
speed = 10703437
dist = 0

for t in terrain:
    speed -= brake_factor_km[t]
    dist += 1

    if speed <= 0:
        print(dist)
        break

    brake_factor_km['I'] = brake_factor_km['I'] - 12 if t == 'I' else -12

    if t == 'F':
        brake_factor_km['F'] = -35 if brake_factor_km['F'] == 70 else 70
