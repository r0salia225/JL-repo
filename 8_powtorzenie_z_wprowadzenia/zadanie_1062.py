t = int(input())

for i in range(t):
    c, d, e = map(int, input().split())
    tab = []
    for i in range(2, c):
        if i % d == 0 and i % e != 0:
            tab.append(i)
    print("".join(map(str, tab)))

    #gaderypoluki, chekoladka, koniecmatury, cezar, morse, malinowebuty