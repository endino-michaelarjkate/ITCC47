l = [1, 0, 2, -10, 0, 9] 
# #  l = [-1, 9, 10, 8, 0, 0]

def zeroShift(l):
    i = 0 
    right_idx = len(l) - 1
    while i < len(l):
        left_idx = i
        # if l[i] == 0 and l[swap_index] != 0:
        #     l[i], l[swap_index] = l[swap_index], l[i] 
        # swap_index -= 1 
        # i += 1 
        if l[left_idx] == 0 and l[right_idx] != 0:
            l[left_idx], l[right_idx] = l[right_idx], l[left_idx] 
        right_idx -= 1
        i += 1

    # i = 0 
    # while i < len(l)-1:
    #     prev = 0
    #     if (l[i] == 0 and l[i+1] != 0) or l[i] == 0:
    #         l[i], l[i+1] = l[i+1], l[i] 
    #     i += 1

l = [1, 0, 2, -10, 0, 9]
zeroShift(l)
print(l)
m = [1, 0, 0, 2, -10, 0, 0]
zeroShift(m)
print(m)

# def x(l: int,m: int, n: int):
#     # return (((m-1) + (l-1))%n)+1
#     m -= 1
#     l -= 1
#     sum = m+l 
#     sum = (sum % n) + 1 
#     return sum 


# print(x(1,2,3))
     

# print(x(l))