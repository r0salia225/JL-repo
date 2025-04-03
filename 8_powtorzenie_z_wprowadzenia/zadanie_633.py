with open('dane_napisy_3.txt') as f:
    linie = [x.split() for x in f.readlines()]

    #print(linie)


def jednolity(napis):
    for i in range(1, len(napis)):
        if napis[0] != napis[i]:
            return False
    return True

def anagramy(napis1,  napis2):
    litery = [0]*26
    for i in range(len(napis1)):
        nr = ord(napis1[i]) - ord('A')
        litery[nr] += 1
        nr = ord(napis2[i]) - ord('A')
        litery[nr] -= 1
    for w in litery:
        if w != 0:
            return False
    return True


ilosc = 0
anagramow = 0
for A, B in linie:
    if len(A) != len(B):
        continue
    if jednolity(A) and A == B:
        ilosc += 1
    if anagramy(A, B):
        anagramow += 1

print("A)", ilosc)
print("B)", anagramow)
print("C)", )

for A, B in range(len(linie)):
    for j in range(i+)
