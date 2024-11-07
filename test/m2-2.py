import pytest
from io import StringIO
import sys

def binary_search(a, x):
    left = 0
    right = len(a) - 1

    while left < right:
        mid = (left + right) // 2
        if a[mid] > x:
            left = mid + 1
        else:
            right = mid

    if left == right and a[left] == x:
        return left
    else:
        return -1
    

# 입력을 모의하기 위한 유틸리티 함수
# 입력을 모의하기 위한 유틸리티 함수
def run_test(input_data, expected_output):
    original_stdin = sys.stdin  # 원래의 stdin 저장
    original_stdout = sys.stdout  # 원래의 stdout 저장
    try:
        sys.stdin = StringIO(input_data)  # 입력을 가상으로 설정
        sys.stdout = StringIO()  # 출력을 가상으로 설정

        # 메인 로직 실행 (입력 처리 및 결과 출력 부분)
        n, k = input().split()
        n = int(n)
        k = int(k)

        list_for_n = []
        list_for_k = []

        for i in range(n):
            a = int(input())
            list_for_n.append(a)

        for j in range(k):
            q = int(input())
            list_for_k.append(q)

        for d in list_for_k:
            print(binary_search(list_for_n, d))
        
        result = sys.stdout.getvalue()  # 가상 출력 내용을 저장

        assert result.strip() == expected_output.strip()  # 출력 결과와 기대 결과를 비교
    finally:
        sys.stdin = original_stdin  # stdin 복구
        sys.stdout = original_stdout  # stdout 복구


# 기본적인 정상 동작 테스트
@pytest.mark.timeout(3)
def test_basic_case():
    input_data = """5 1
90
80
70
60
50
50"""
    expected_output = "4"
    run_test(input_data, expected_output)

# 값이 수열의 첫 번째에 있는 경우
@pytest.mark.timeout(3)
def test_first_value():
    input_data = """5 1
90
80
70
60
50
90"""
    expected_output = "0"
    run_test(input_data, expected_output)

# 값이 수열의 마지막에 있는 경우
@pytest.mark.timeout(3)
def test_last_value():
    input_data = """5 1
90
80
70
60
50
50"""
    expected_output = "4"
    run_test(input_data, expected_output)

# 값이 수열에 없는 경우
@pytest.mark.timeout(3)
def test_value_not_found():
    input_data = """5 1
90
80
70
60
50
40"""
    expected_output = "-1"
    run_test(input_data, expected_output)

# 여러 개의 질의 테스트
@pytest.mark.timeout(3)
def test_multiple_queries():
    input_data = """5 3
90
80
70
60
50
90
60
40"""
    expected_output = """0
3
-1"""
    run_test(input_data, expected_output)

# 성능 테스트 (최대 범위 값)
@pytest.mark.timeout(3)
def test_large_input():
    # 100,000개의 내림차순 수열 생성
    n = 100000
    input_data = f"{n} 1\n"
    input_data += "\n".join(str(i) for i in range(n, 0, -1))  # n부터 1까지의 수열
    input_data += "\n1"  # 질의 값
    
    expected_output = f"{n - 1}"  # 마지막 인덱스에서 값 1을 찾아야 함
    
    run_test(input_data, expected_output)

### 추가 엣지 케이스들 ###

# 수열이 1개만 있을 때
@pytest.mark.timeout(3)
def test_single_element():
    input_data = """1 1
50
50"""
    expected_output = "0"
    run_test(input_data, expected_output)

# 수열에 값이 없을 때
@pytest.mark.timeout(3)
def test_single_element_not_found():
    input_data = """1 1
50
100"""
    expected_output = "-1"
    run_test(input_data, expected_output)

# 질의 중복: 같은 값을 여러 번 질의
@pytest.mark.timeout(3)
def test_duplicate_queries():
    input_data = """5 3
90
80
70
60
50
60
60
60"""
    expected_output = """3
3
3"""
    run_test(input_data, expected_output)

# 질의가 수열보다 모두 큰 값일 때
@pytest.mark.timeout(3)
def test_query_larger_than_all():
    input_data = """5 2
90
80
70
60
50
100
95"""
    expected_output = """-1
-1"""
    run_test(input_data, expected_output)

# 질의가 수열보다 모두 작은 값일 때
@pytest.mark.timeout(3)
def test_query_smaller_than_all():
    input_data = """5 2
90
80
70
60
50
40
10"""
    expected_output = """-1
-1"""
    run_test(input_data, expected_output)

# 값이 존재하지 않는 여러 질의 테스트
@pytest.mark.timeout(3)
def test_multiple_queries_not_found():
    input_data = """5 3
90
80
70
60
50
100
30
20"""
    expected_output = """-1
-1
-1"""
    run_test(input_data, expected_output)

# 질의가 모두 수열 내에 존재하는 경우
@pytest.mark.timeout(3)
def test_all_queries_found():
    input_data = """5 3
90
80
70
60
50
90
50
60"""
    expected_output = """0
4
3"""
    run_test(input_data, expected_output)

# 질의가 일부 존재하고, 일부는 존재하지 않는 경우
@pytest.mark.timeout(3)
def test_some_queries_found_some_not():
    input_data = """5 4
90
80
70
60
50
70
10
90
30"""
    expected_output = """2
-1
0
-1"""
    run_test(input_data, expected_output)

# 수열이 짧고 질의가 여러 개 주어진 경우
@pytest.mark.timeout(3)
def test_short_sequence_many_queries():
    input_data = """3 5
30
20
10
30
10
50
20
5"""
    expected_output = """0
2
-1
1
-1"""
    run_test(input_data, expected_output)

def test_same_queries():
    input_data = """5 3
90
80
70
60
50
50
50
50"""
    expected_output = """4
4
4"""
    run_test(input_data, expected_output)


def test_mixed_queries():
    input_data = """5 4
100
90
80
70
60
90
100
30
50"""
    expected_output = """1
0
-1
-1"""
    run_test(input_data, expected_output)


def test_large_queries_no_match():
    n = 100000
    input_data = f"{n} 5\n"
    input_data += "\n".join(str(i) for i in range(n, 0, -1)) + "\n"
    input_data += "100001\n100002\n100003\n100004\n100005"
    expected_output = "-1\n-1\n-1\n-1\n-1"
    run_test(input_data, expected_output)

@pytest.mark.timeout(5)
def test_maximum_input_size():
    n = 100000
    k = 100000
    input_data = f"{n} {k}\n"
    input_data += "\n".join(str(i) for i in range(n, 0, -1)) + "\n"
    input_data += "\n".join(str(i) for i in range(1, k + 1))
    expected_output = "\n".join(str(n - i) if i <= n else "-1" for i in range(1, k + 1))
    run_test(input_data, expected_output)

@pytest.mark.timeout(3)
def test_minimum_input_size():
    input_data = """1 1
50
50"""
    expected_output = "0"
    run_test(input_data, expected_output)

@pytest.mark.timeout(3)
def test_all_same_values():
    input_data = """5 3
50
50
50
50
50
50
40
60"""
    expected_output = """0
-1
-1"""
    run_test(input_data, expected_output)


@pytest.mark.timeout(3)
def test_arithmetic_sequence():
    input_data = """5 3
100
90
80
70
60
80
50
110"""
    expected_output = """2
-1
-1"""
    run_test(input_data, expected_output)


@pytest.mark.timeout(3)
def test_uniformly_distributed_queries():
    n = 100
    k = 10
    numbers = list(range(n, 0, -1))
    queries = [numbers[i * (n // k)] for i in range(k)]
    input_data = f"{n} {k}\n"
    input_data += "\n".join(map(str, numbers)) + "\n"
    input_data += "\n".join(map(str, queries))
    expected_output = "\n".join(map(str, [numbers.index(q) for q in queries]))
    run_test(input_data, expected_output)

@pytest.mark.timeout(3)
def test_queries_concentrated_at_ends():
    n = 100
    k = 10
    numbers = list(range(n, 0, -1))
    queries = [numbers[i] for i in range(k // 2)] + [numbers[-i - 1] for i in range(k // 2)]
    input_data = f"{n} {k}\n"
    input_data += "\n".join(map(str, numbers)) + "\n"
    input_data += "\n".join(map(str, queries))
    expected_output = "\n".join(map(str, [numbers.index(q) for q in queries]))
    run_test(input_data, expected_output)

import random

@pytest.mark.timeout(5)
def test_random_input():
    import random
    n = random.randint(1, 100000)
    k = random.randint(1, 100000)
    
    # 중복 없는 랜덤 수열을 만들고 내림차순 정렬
    numbers = sorted(random.sample(range(1, 2 * n + 1), n), reverse=True)
    
    # 딕셔너리로 숫자와 인덱스 매핑
    number_index = {num: idx for idx, num in enumerate(numbers)}
    
    # 질의 생성
    queries = random.sample(range(1, 2 * n + 1), k)
    
    input_data = f"{n} {k}\n"
    input_data += "\n".join(map(str, numbers)) + "\n"
    input_data += "\n".join(map(str, queries))
    
    # expected_output 생성 (딕셔너리에서 값 탐색)
    expected_output = "\n".join(str(number_index[q]) if q in number_index else "-1" for q in queries)
    
    run_test(input_data, expected_output)

