l = [-9, 5, 7, 3, 0, 100, 20]

# i = 1
# while i < len(l):
#     a = l[i] # reserve the value of the current element

#     j = i - 1
#     while j >= 0 and a < l[j]: # checks if current element is lesser than the elements of the sorted part of the array
#         l[j+1] = l[j] # adjusts the list to make room for current element at its position
#         j -= 1 
    
#     l[j+1] = a  # inserts element at correct position 
#     i += 1 
 
print(l) 


l = [-9, 5, 7, 3, 0, 100, 20]

i = 1
while i < len(l):
    a = l[i]
    j = i - 1
    while j >= 0 and a < l[j]:
        l[j+1] = l[j] 
        j -= 1
    l[j+1] = a 
    i += 1 

print(l) 



