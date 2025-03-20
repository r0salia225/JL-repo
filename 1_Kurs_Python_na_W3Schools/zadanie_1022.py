# Wczytanie dwóch liczb
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

# Zamiana miejscami, aby a było zawsze mniejsze lub równe b
if a > b:
    a, b = b, a

# Zmienna przechowująca sumę
suma = 0
aktualna_wartosc = a

# Pętla, która liczy sumę ciągu geometrycznego
while aktualna_wartosc <= b:
    suma += aktualna_wartosc
    aktualna_wartosc *= 1.45

# Wyświetlenie wyniku
print(f"Suma ciągu geometrycznego wynosi: {suma}")