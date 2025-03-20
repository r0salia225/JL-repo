# Funkcja obliczająca drogę w spadku swobodnym
def droga_spadku(t):
    g = 9.81  # Przyspieszenie ziemskie w m/s^2
    s = 0.5 * g * t**2  # Wzór na drogę w spadku swobodnym
    return s

# Wczytanie czasu od użytkownika
czas = float(input("Podaj czas spadania w sekundach: "))

# Obliczenie drogi
d = droga_spadku(czas)

# Wyświetlenie wyniku
print(f"Droga przebyta przez ciało w czasie {czas} sekund to: {d:.2f} metrów")
