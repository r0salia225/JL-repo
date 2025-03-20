import math

# Wczytanie liczby całkowitej x od użytkownika
try:
    x = int(input("Podaj liczbę całkowitą x: "))
    
    # Sprawdzamy, czy wyrażenie pod pierwiastkiem jest nieujemne
    if x < 0:
        print("Nie mogę obliczyć pierwiastka z liczby ujemnej w zbiorze liczb rzeczywistych.")
    else:
        # Obliczanie wartości wyrażenia: 3 * sqrt(-x^5) - 2 + x
        result = 3 * math.sqrt(-x**5) - 2 + x
        print(f"Wartość wyrażenia dla x = {x} wynosi: {result}")
except ValueError:
    print("Podaj prawidłową liczbę całkowitą!")
except Exception as e:
    print(f"Wystąpił błąd: {e}")