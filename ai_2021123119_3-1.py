def computeFailNaive(pat : list) -> list:
    f = [0 for i in range(len(pat))]
    for i in range(len(pat)):
        f[i] = 0
        for j in range(i, 0, -1):
            matched = True
            for k in range(j):
                if pat[k] != pat[i- (j - 1) + k]:
                    matched = False
                    break
            if matched:
                f[i] = j
                break
    return f

def kmpMatch(seq : list , pat : list, f : list) -> int:
    posT, posP, lastT = 0,0,0
    n,m = len(seq), len(pat)
    islast = False
    while (posT < n) and (posP<m):
        if seq[posT] == pat[posP]:
            posT += 1
            posP += 1
            if posP == m :
                lastT = posT
                islast = True
                posP = f[posP-1]
        else:
            if posP == 0:
                posT += 1
            else :
                posP = f[posP-1]
    if (not islast) and (posP < m) : return -1
    else : return lastT - m

n, m = input().split()
n = int(n)
m = int(m)

list_for_n = []
list_for_m = []

for i in range(n):
    a = int(input().strip())
    list_for_n.append(a)

for j in range(m):
    b = int(input().strip())
    list_for_m.append(b)

f = computeFailNaive(list_for_m)
result = kmpMatch(list_for_n, list_for_m, f)

print(result)