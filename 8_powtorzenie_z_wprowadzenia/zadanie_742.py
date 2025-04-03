x = int(input())


for i in range(x):
    data = list(map(int, input().split()))
    n = data[0]
    numbers = data[1:]
    print(numbers)

    niep_arzyste = [numbers[i] for i in range(n) if (i + 1) % 2 == 0]
    p_arzyste = [numbers[i] for i in range(n) if (i + 1) % 2 != 0]


print(p_arzyste, niep_arzyste)