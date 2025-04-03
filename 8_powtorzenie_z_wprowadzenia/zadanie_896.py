with open('godziny_pracy.txt') as f:
    czasStr = [x.split() for x in f.readlines()]

    f.close()
    print(czasStr)


def czas(godz):
    strG, strM = godz.split(':')
    g = int(strG)
    m = int(strM)
    return g + m / 60


praca = 0

for poczatek, koniec in czasStr:
    pCzas = czas(poczatek)
    kCzas = czas(koniec)
    praca += kCzas - pCzas

    print(round(praca, 2))






