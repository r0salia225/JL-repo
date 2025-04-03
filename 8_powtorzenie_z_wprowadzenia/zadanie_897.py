with open("ciagi_liter.txt") as f:
    plik = [x.split() for x in f.readlines()]

    f.close()
    #print(plik)

"""
litery = [0]*26
A = 0
for linia in plik:
    for litera in linia:
        if litera == litery:
            A += 1
    print(A)
"""
liter = 0
for s in plik:
    liter += len(s)

print("A)", liter)

max = 0

for i in range(len(plik)):
    if len(plik[i]) > len(plik[max]):
        max = i

print("B)", len(plik[max]))

def najczestsza(slowo):
    alf = [0]*26
    for l in plik:
        x = ord("L") - ord("A")
        tab[x] += 1
    m = 0
    for t in tab