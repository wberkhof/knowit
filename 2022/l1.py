
def translate_letter(l: str, d: dict):
    l_english = []
    l_offset = 0

    while l_offset < len(l):
        r_offset = len(l)

        while not l[l_offset:r_offset] in d:
            r_offset-=1

        l_english.append(d[l[l_offset:r_offset]])

        l_offset = r_offset
    
    return(l_english)

def main():
    with open('2022/l1_dictionary.txt', 'r', encoding='utf-8') as dict_in:
        d = {line.split(',')[0]: line.split(',')[1].rstrip('\n') for line in dict_in.readlines()}

    with open('2022/l1_letter.txt', 'r', encoding='utf-8') as letter_in:
        l = letter_in.read()

    l_english = translate_letter(l, d)

    result = ' '.join(l_english)

    print(result, len(result))

main()