l = [-9, 5, 7, 3, 0, 100, 20]

# using selection sort:

i = 0 
while i < len(l) - 1:
    swap_index = i 
    j = i + 1 
    while j < len(l):
        if l[swap_index] < l[j]:
            swap_index = j 
        j += 1
    l[i], l[swap_index] = l[swap_index], l[i]
    i += 1 

print(l)

# using bubble sort
l = [-9, 5, 7, 3, 0, 100, 20]
x = 0
while x < len(l):
    y = x 
    while y < len(l)-x-1:
        if l[y] < l[y+1]:
            l[y], l[y+1] = l[y+1], l[y] 
        y += 1
    x += 1 

print(l)  

# using insertion sort 
l = [-9, 5, 7, 3, 0, 100, 20]
i = 1 
while i < len(l):
    a = l[i] 
    j = i - 1
    while j >= 0 and a > l[j]:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = a
    i += 1

print(l)
