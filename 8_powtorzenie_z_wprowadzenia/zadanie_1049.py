with open("uczniowie2.txt") as f:
    uczniowie = [x.split() for x in f.readlines()]

#print(uczniowie)

for i in range(len(uczniowie)):
    for j in range(3, len(uczniowie[i])):
        uczniowie[i][j] = float(uczniowie[i][j])

print(uczniowie)
"""
klasy = [0]*4

for uczen in uczniowie:
    nr = ord(uczen[2]) - ord('A')
    klasy[nr] += 1 
print('A)')
for i in range(len(klasy)):
    print(' ', chr(65+i), klasy[i])


maxWpl= 0
iin = 0
sumaWpl = 0
minJedWpl = 10000000000
maxJedWpl = 0
for uczen in uczniowie:
    x = 0
    for i in range(3, len(uczen)):
        x += uczen[i]
        if minJedWpl > uczen[i]:
            minJedWpl = uczen[i]
        if maxJedWpl < uczen[i]:
            maxJedWpl = uczen[i]
    sumaWpl += x
    if maxWpl < x:
        maxWpl = x
        iin = uczen[0] + '' + uczen[1]
print('B)')
print(' ', iin, maxWpl)
print('C)')
print(' ', round(sumaWpl, 2))
print('D)')
print(' ', minJedWpl, maxJedWpl)"""