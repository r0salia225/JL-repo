# Wczytanie dwóch liczb od użytkownika
liczba = int(input("Podaj pierwszą liczbę: "))
powtorzenia = int(input("Podaj drugą liczbę (ile razy chcesz wykonać mnożenie): "))

# Wydrukowanie kolejnych iloczynów
wynik = liczba
for i in range(powtorzenia):
    print(wynik)
    wynik *= liczba  # Kolejne mnożenie przez pierwszą liczbę