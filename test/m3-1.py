def test_long_repeating_sequence_debug():
    n = 20  # 작은 값으로 테스트
    m = 3
    pat = [1, 2, 3]
    
    # 시퀀스: [1, 2] 반복, 마지막 m 요소를 패턴으로 대체하여 길이 n 유지
    seq = [1, 2] * (n // 2)
    seq[-m:] = pat  # 마지막 m개의 요소를 패턴으로 대체

    # 시퀀스와 패턴을 먼저 출력
    print(f"Sequence (first {n} items): {seq[:n]}")
    print(f"Pattern: {pat}")
    
    # 매칭을 위한 준비
    input_lines = [f"{n} {m}"] + [str(num) for num in seq[:n]] + [str(num) for num in pat]
    input_data = "\n".join(input_lines)
    list_for_n = [int(num) for num in seq[:n]]
    list_for_m = [int(num) for num in pat]

    # 실패 함수 (failure function) 계산
    def computeFailNaive_debug(pat):
        f = [0 for _ in range(len(pat))]
        for i in range(len(pat)):
            f[i] = 0
            for j in range(i, 0, -1):
                matched = True
                for k in range(j):
                    if pat[k] != pat[i - (j - 1) + k]:
                        matched = False
                        break
                if matched:
                    f[i] = j
                    break
        return f

    # KMP 매칭 수행, 매칭 과정을 출력
    def kmpMatch_debug(seq, pat, f):
        posT, posP, lastT = 0, 0, 0
        n, m = len(seq), len(pat)
        islast = False
        while posT < n and posP < m:
            if seq[posT] == pat[posP]:
                posT += 1
                posP += 1
                print(f"Match found so far at posT: {posT}, posP: {posP}")
                if posP == m:
                    print(f"Pattern found ending at posT: {posT}, resetting posP using failure function")
                    lastT = posT
                    islast = True
                    posP = f[posP - 1]
            else:
                if posP == 0:
                    posT += 1
                else:
                    posP = f[posP - 1]
                print(f"No match, moving to posT: {posT}, posP: {posP}")
        if not islast and posP < m:
            return -1
        else:
            return lastT - m

    # 실패 함수 계산 및 패턴 매칭 시작
    f = computeFailNaive_debug(list_for_m)
    result = kmpMatch_debug(list_for_n, list_for_m, f)

    # 최종 결과 출력
    print(f"Result: {result}")

# 실행
test_long_repeating_sequence_debug()
