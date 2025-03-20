# Kursy walut (stan na 20.03.2025)
KURS_EURO = 4.1581  # 1 EUR = 4.1581 PLN
KURS_DOLAR = 3.8067  # 1 USD = 3.8067 PLN

# Wczytanie kwoty w złotówkach od użytkownika
zlote = float(input("Podaj kwotę w złotówkach: "))

# Obliczenie wartości w euro i dolarach
euro = zlote / KURS_EURO
dolar = zlote / KURS_DOLAR

# Wyświetlenie wyników
print(f"{zlote} PLN to {euro:.2f} EUR lub {dolar:.2f} USD")
