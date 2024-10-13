l = [2,3,-4,0,6,7,]

def Min(A,n):
    reserve = A[0]
    for i in range(1,n):
        if reserve > A[i]:
            reserve = A[i]
    return reserve 
    
Min(l,4) 
