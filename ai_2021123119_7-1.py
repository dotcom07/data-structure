def insertSort(a, n):
    for i in range(n):
        tmp = a[i]
        j = i - 1
        while j >= 0:
            if a[j] >= tmp: break
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp
        
k = int(input())
nums = []

for i in range(k):
    n = int(input())
    nums.append(n)

insertSort(nums, len(nums))

for n in nums:
    print(n)