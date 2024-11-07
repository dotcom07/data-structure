def computeFailNaive(pat : str) -> list:
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

def kmpMatch(seq : str , pat : str, f : list) -> int:
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
                posP = 0
        else:
            if posP == 0:
                posT += 1
            else :
                posP = f[posP-1]
    if (not islast) and (posP < m) : return -1
    else : return lastT -m




    # Example 1
pat = "ABABC"
seq = "ABABABABCABABABC"
f = computeFailNaive(pat)
print("Failure function:", f)
result = kmpMatch(seq, pat, f)
print("Result:", result)

# Example 2
pat = "TEST"
seq = "THISISATESTTEXT"
f = computeFailNaive(pat)
print("Failure function:", f)
result = kmpMatch(seq, pat, f)
print("Result:", result)

# Example 3
pat = "AABA"
seq = "AABAACAADAABAABA"
f = computeFailNaive(pat)
print("Failure function:", f)
result = kmpMatch(seq, pat, f)
print("Result:", result)

seq = ""
pat = "A"
f = computeFailNaive(pat)  # 실패 함수 계산
print(kmpMatch(seq, pat, f))  # 예상 결과: -1

seq = "A"
pat = "B"
f = computeFailNaive(pat)  # 예상 결과: [0] (패턴이 없으므로 실패 함수도 빈 리스트)
print(kmpMatch(seq, pat, f))  # 예상 결과: 0 (빈 패턴은 언제나 처음 위치에서 매칭)

seq = "A"
pat = "ABC"
f = computeFailNaive(pat)
print(kmpMatch(seq, pat, f))  # 예상 결과: -1


seq = "ABABCABABC"
pat = "ABABC"
f = computeFailNaive(pat)
print(kmpMatch(seq, pat, f))  # 예상 결과: 5 (마지막으로 일치한 패턴의 시작 위치)

seq = "ABCD"
pat = "BCD"
f = computeFailNaive(pat)
print(kmpMatch(seq, pat, f))  # 예상 결과: 1

seq = "AAABAAA"
pat = "AAAA"
f = [0, 1, 2, 3]  # 잘못된 실패 함수
print(kmpMatch(seq, pat, f))  # 잘못된 실패 함수 사용, 예상 결과는 잘못된 값

seq = "AABC"
pat = "ABC"
f = computeFailNaive(pat)
print(kmpMatch(seq, pat, f))  # 예상 결과: 1 (첫 번째 문자부터 부분적으로 일치)

seq = "ABCDE"
pat = "XYZ"
f = computeFailNaive(pat)
print(kmpMatch(seq, pat, f))  # 예상 결과: -1
