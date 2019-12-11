import re
from time import strptime

with open("logg.txt", "r") as f:
    logg = f.read()

forbruk = r"\s+\* (\d+) (?:meter|ml) (tannkrem|toalettpapir|sjampo)"
pattern = re.compile(r"(?P<dato>[A-Z][a-z]{2} \d{2}):" + forbruk * 3)


def add_to(item: str, match):
    """Finds index of item, and return the captured group just before,
    which happens to be the amount."""
    return int(match.group(match.groups().index(item)))


sjampo = 0
tannkrem = 0
toalettpapir = 0
søndag_sjampo = 0
onsdag_toalettpapir = 0

for m in pattern.finditer(logg):
    add_sjampo = add_to("sjampo", m)
    add_toalettpapir = add_to("toalettpapir", m)

    toalettpapir += add_toalettpapir
    sjampo += add_sjampo
    tannkrem += add_to("tannkrem", m)

    dato = strptime("2018 " + m.group("dato"), "%Y %b %d")
    if dato.tm_wday == 6:  # søndag
        søndag_sjampo += add_sjampo
    elif dato.tm_wday == 2:  # onsdag
        onsdag_toalettpapir += add_toalettpapir


print(
    (sjampo // 300)
    * søndag_sjampo
    * (tannkrem // 125)
    * (toalettpapir // 25)
    * onsdag_toalettpapir
)