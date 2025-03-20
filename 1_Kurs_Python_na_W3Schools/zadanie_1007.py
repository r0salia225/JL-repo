# Program do wydrukowania tabliczki mnożenia 10x10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:2}", end=" ")  # Wydrukowanie wyniku z odpowiednim odstępem
    print()  # Nowa linia po każdej iteracji