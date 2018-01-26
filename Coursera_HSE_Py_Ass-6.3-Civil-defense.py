n = int(input())
ln = list(map(int, input().split()))
m = int(input())
lm = list(map(int, input().split()))
lnn = []
lmm = []
to = []
o = []
oo = []

for i in range(0, n):
    t = (i + 1, ln[i])
    lnn.append(t)
    lnn.sort()

for i in range(0, m):
    t = (i + 1, lm[i])
    lmm.sort()
    lmm.append(t)

for i in range(n):
    for j in range(m):
        if lnn[i][1] - lmm[j][1] >= 0:
            to.append(lnn[i][1] - lmm[j][1])
        else:
            to.append(-1 * (lnn[i][1] - lmm[j][1]))

for i in range(0, len(to), m):
    too = tuple(to[i:i+m])
    o.append(too)

for i in range(len(o)):
    j = o[i]
    oo.append(j.index(min(j)) + 1)

print(' '.join(map(str, oo)))
