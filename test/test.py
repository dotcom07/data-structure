import time
import random

# 테스트에 사용할 입력 크기
n = 50000

# 랜덤한 테스트 케이스 생성 (-1000000 ~ 1000000 범위의 정수)
test_case = [random.randint(-1000000, 1000000) for _ in range(n)]

# 내림차순 정렬 프로그램 함수
def mergeSort(a, n):
    aux = [0 for _ in range(len(a))]
    doMergeSort(a, 0, n - 1, aux)

def doMergeSort(a, left, right, aux):
    if left >= right:
        return
    mid = (left + right) // 2
    doMergeSort(a, left, mid, aux)
    doMergeSort(a, mid + 1, right, aux)

    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if a[i] >= a[j]:
            aux[k], k, i = a[i], k + 1, i + 1
        else:
            aux[k], k, j = a[j], k + 1, j + 1

    while i <= mid:
        aux[k], k, i = a[i], k + 1, i + 1
    while j <= right:
        aux[k], k, j = a[j], k + 1, j + 1

    for i in range(left, right + 1):
        a[i] = aux[i]

# 성능 측정
start_time = time.time()

# 정렬 수행
mergeSort(test_case, len(test_case))

end_time = time.time()
execution_time = end_time - start_time

# 결과 출력
print(f"실행 시간: {execution_time:.4f}초")
