def mergeSort(a, n):
    aux = [0 for i in range(len(a))]
    doMergeSort(a, 0, n - 1, aux)

def doMergeSort(a, left, right, aux):
    if left >= right: return
    mid = (left + right) // 2
    doMergeSort(a, left, mid, aux) 
    doMergeSort(a, mid + 1, right, aux)

    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if a[i] >= a[j]: aux[k], k, i = a[i], k+1, i+1
        else           : aux[k], k, j = a[j], k+1, j+1

    while i <= mid     : aux[k], k, i = a[i], k+1, i+1
    while j <= right   : aux[k], k, j = a[j], k+1, j+1

    for i in range(left, right+1): a[i] = aux[i]

        
k = int(input())
nums = []

for i in range(k):
    n = int(input())
    nums.append(n)

mergeSort(nums, len(nums))

for n in nums:
    print(n)