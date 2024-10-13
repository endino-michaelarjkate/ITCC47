def maxProd(integers: list):
    max1 = integers[0]
    max2 = integers[1]
    min1 = 0
    min2 = 0


    if max2 > max1:
        max1, max2 = max2, max1
    
    i = 2
    while i < len(integers):
        if integers[i] > max1:
            max2 = max1
            max1 = integers[i]
        elif integers[i] < 0:
            if min1 != 0:
                min2 = integers[i]
            elif integers[i] < min1:
                min2 = min1
                min1 = integers[i]
        i += 1

    maxProd = max1 * max2
    minProd = min1 * min2

    if maxProd > minProd:
        return maxProd
    else:
        return minProd 
    

list1 = [1,2,-9,-9,10,8,0] # 81
list2 = [1,2,-9,9,10,8,0] # 90
list3 = [1,2,9,20,10,8,0] #200

print(maxProd(list1))
print(maxProd(list2))
print(maxProd(list3))


"""
ALGORITHM:
    1. receive list of integers
    2. create max1, max2 variables and initialize it to the first 2 elements of the list
    3. create min1, min2 variables and initialize it to 0. this is to store negative elements later
    4. check if max2>max1, if yes swap the values 
    5. iterate over the remaining elements of the list, and check if an element is > max 1, if yes, update the values of max1 to the element, and max2 to max1 
    6. if an element is < 0, update the values of min1 and min2 
    7. calculate products of min1 and min2, and max1 and max2
    8. compare which is greater, and return it 
"""