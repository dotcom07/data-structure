import pytest
import time
import numpy as np

def answer_Q(n, i, j):  # 수정 금지
    if n == 0:
        return 1
    else:
        size = 3**n
        batch = int(size / 3)
        if (i <= batch and j <= batch):
            return answer_Q(n-1, i, j)
        elif (i <= batch and (size - (batch - 1) <= j <= size)):
            return answer_Q(n-1, i, j - (batch * 2))
        elif (1 + batch <= i <= batch + batch) and (1 + batch <= j <= batch + batch):
            return answer_Q(n-1, i - batch, j - batch)
        elif ((size - (batch - 1) <= i <= size) and j <= batch):
            return answer_Q(n-1, i - (batch * 2), j)
        elif ((size - (batch - 1) <= i <= size) and (size - (batch - 1) <= j <= size)):
            return answer_Q(n-1, i - (batch * 2), j - (batch * 2))
        else:
            return (2*(n-1)+3)

def generate_matrix_A(n):
    if n == 0:
        # Base case A(0)
        return np.array([[1]])
    else:
        # Recursive case: generate A(n-1) and B(n-1)
        A_n = generate_matrix_A(n - 1)
        B_n = np.full(A_n.shape, 2 * (n - 1) + 3)
        
        # Stack matrices to form A(n)
        top = np.hstack([A_n, B_n, A_n])
        middle = np.hstack([B_n, A_n, B_n])
        bottom = np.hstack([A_n, B_n, A_n])
        
        return np.vstack([top, middle, bottom])

@pytest.mark.timeout(1)  # 각 테스트 케이스는 1초 이내에 완료되어야 함
def test_answer_Q():
    for n in range(0, 6):  # 모든 행렬에 대해서 테스트
        matrix_a = generate_matrix_A(n)  # 정답 행렬 생성
        size = len(matrix_a)  # 행렬 크기 확인
        for i in range(1, size+1):  # 각 행에 대해
            for j in range(1, size+1):  # 각 열에 대해
                start_time = time.time()  # 시작 시간 기록
                result = answer_Q(n, i, j)  # 테스트할 함수 호출
                end_time = time.time()  # 끝난 시간 기록
                assert end_time - start_time <= 1, f"Timeout: n={n}, i={i}, j={j}"  # 1초 안에 끝났는지 확인
                assert result == matrix_a[i-1][j-1], f"Wrong answer: n={n}, i={i}, j={j}, expected={matrix_a[i-1][j-1]}, result={result}"  # 값이 일치하는지 확인

if __name__ == "__main__":
    pytest.main()
