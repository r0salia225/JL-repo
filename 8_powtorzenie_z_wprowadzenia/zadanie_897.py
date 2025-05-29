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




    tab = [3, 6, 7, 2, 8, 4, 1]
print(tab)

ile = 0
n = len(tab)
for i in range(len(tab)):
    posortowane = True
    for j in range(n-1):
        ile += 1
        if tab[j] > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab[j]
            posortowane = False
        if posortowane:
            break
    n -= 1

print(tab)
print(ile)


tab = [3, 2, 6, 1, 8, 2, 9]

n = len(tab)
i = n
k = 0

for j in range(n):
    i = n - 1
    t = tab[i]
    while i > k:
        if t < tab[i-1]:
            tab[i] = tab[i - 1]
        else:
            t, tab[i] = tab[i - 1], t
        i -= 1
    tab[k] = t
    k += 1

print(tab)



tab = [1, 9, 2, 8, 3, 7, 4, 5, 6]

tab2 = []
n = len(tab)
for i in range(n):
    I = 0
    for j in range(len(tab)):
        if tab[j] < tab[I]:
            I = j

    tab2.append(tab[I])
    del tab[I]

print(tab2)
print(tab)
