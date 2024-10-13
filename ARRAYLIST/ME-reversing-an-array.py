l = [1,20,3,4,5,86,7,8,9,108,11] 
# l = [10,9,8,7,6,6,4,3,2,1]  
def reverseArr(arr: 'list'): 
    i = 0 
    swap_index = len(arr)-1
    while swap_index > i:
        arr[swap_index], arr[i] = arr[i], arr[swap_index]
        i += 1
        swap_index -= 1

reverseArr(l)
print(l)




def reverse(A):
    i = 0
    k = len(A) - 1
    while i < k:
        temp = A[i]
        A[i] = A[k]
        A[k] = temp 
        i += 1
        k -= 1 

reverse(l)
print(l)

