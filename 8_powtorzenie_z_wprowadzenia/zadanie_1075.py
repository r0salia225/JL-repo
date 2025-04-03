t = int(input())

s = 0
napis = []
for i in range(t):
    v1, v2 = map(int, input().split())
    s = (2*v1 *v2) // (v1 + v2)
    napis.append(str(s))

print("\n".join(napis))


