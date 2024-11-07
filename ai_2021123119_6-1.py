def answer_Q(n,i,j):
    if n == 0:
        return 1
    else:
        size = 3**n
        batch = size // 3
        if (i <=batch and j<=batch):
            return answer_Q(n-1,i,j)
        elif ( i <=batch and  (size-(batch-1) <= j <= size) ) :
            return answer_Q(n-1,i, j - ( batch * 2 ))
        elif (1+batch <= i <=batch+batch) and (1+batch <= j <= batch+batch ) :
            return answer_Q(n-1,i - batch, j - batch)
        elif ( (size-(batch-1) <= i <= size ) and j<=batch) :
            return answer_Q(n-1,i - ( batch * 2 ),j)
        elif ( (size-(batch-1) <= i <= size) and (size-(batch-1) <= j <= size) ) :
            return answer_Q(n-1,i - ( batch * 2 ),j - ( batch * 2 ))
        else :
            return (2*(n-1)+3)
        
k = int(input())

for i in range(k):
    n, i, j = input().split()
    n = int(n)
    i = int(i)
    j = int(j)
    print(answer_Q(n, i, j))