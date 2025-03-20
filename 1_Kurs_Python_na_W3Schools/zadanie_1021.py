# Wczytanie liczb a i b
a = int(input("Podaj pierwszą liczbę (a): "))
b = int(input("Podaj drugą liczbę (b): "))

# Sprawdzenie, czy a jest mniejsze lub równe b
if a > b:
    print("Liczba a musi być mniejsza lub równa liczbie b!")
else:
    # Obliczanie sumy liczb podzielnych przez 3 w zakresie od a do b
    suma = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            suma += i

    # Wypisanie wyniku
    print(f"Suma liczb podzielnych przez 3 od {a} do {b} wynosi: {suma}")