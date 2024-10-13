# create list to store integer inputs
# receive integer inputs and store to the list
# sort the list using selection sort 
# print the elements of the list one by one 

def myFunction(n:int):
    """
    Receives n integers and outputs them in decreasing order.

    Args: n (amount of integer to input)
    """
    l = []
    for i in range(n):
        x = int(input("Enter integer: "))
        l += [x] 
    
    # sort the list 

    for x in range(0,len(l) - 1):
        swap_index = x
        for y in range(x+1,len(l)):
            if l[swap_index] < l[y]:
                swap_index = y
        l[x], l[swap_index] = l[swap_index], l[x]

    for i in l:
        print(i)


myFunction(4)