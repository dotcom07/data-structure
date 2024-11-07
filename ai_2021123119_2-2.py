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
    

n, k = input().split()
n = int(n)
k = int(k)

list_for_n = []
list_for_k = []

for i in range(n) :
    a=int(input())
    list_for_n.append(a)

for j in range(k) :
    q=int(input())
    list_for_k.append(q)

for d in list_for_k:
    print(binary_search(list_for_n, d))