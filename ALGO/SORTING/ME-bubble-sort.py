l = [23,2,1,10] 
# l = [2,1,10,23] 
# l = [1,2,10,23] 

# n = len(l) 
# for i in range(n):
#     for j in range(0, n-i-1):
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j] 

n = len(l)
i = 0 
while i < n:
    j = 0 
    while j < n-i-1:
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
        j += 1
    i += 1

print(l)

def bubbleSort(A): # O(N^2) worst case (reverse sorted input), O(N) best case (sorted input)
    N = len(A)
    while N > 1: # at most n-1 passes
        swapped = False
        for i in range(N-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i] # Python can swap variables like this
                swapped = True
        if not swapped: # optimization
            break
        N -= 1
    return A