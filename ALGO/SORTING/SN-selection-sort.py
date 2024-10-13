# l = [10, -2, 5, 4, 3, 8, 9, 0]

# for i in range(0, len(l) - 1):
#     swap_index = i
#     for j in range(i + 1, len(l)):
#         if l[swap_index] > l[j]:
#             swap_index = j      
#     l[i], l[swap_index] = l[swap_index], l[i]


l = [0,6,4,-100, 4,5,5]

i = 0
while i < len(l) -1:
    swap_index = i 
    j = i + 1
    while j < len(l):
        if l[swap_index] > l[j]:
            swap_index = j
        j += 1
    l[swap_index], l[i] = l[i], l[swap_index]
    i += 1 

print(l)


def selectionSort(A): # O(N^2) for ALL cases...
    N = len(A)
    for L in range(N-1):
        smallest = L + A[L:].index(min(A[L:])) # BEWARE... this is O(N) not O(1)... we cannot find the smallest index of the minimum element of (N-L) items in O(1)
        A[smallest], A[L] = A[L], A[smallest] # Python can swap variables like this
    return A




















