# Napisz program, w którym wczytujesz ilość liczb jakie wylosujesz, a następnie wylosuj tyle liczb całkowitych z przedziału 0-9999 i oblicz ich średnią arytmetyczną.

import random



x = int(input())

suma = 0
random.seed()
for i in range(x):
    liczba = random.randint(0, 10000)
    print(liczba)
    liczba += suma

print(suma/x)