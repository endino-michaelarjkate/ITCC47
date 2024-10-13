# 1. create list to store all permutations of the list
# 2. base case: if len of set == 1, return a  list containing the list 
# 3. iterate over the elements in the list and separate the current element from the remaining elements 
#. 4. recursively call the permutations function with the remaining elements as its argument 
# 5. combine the current element and the remaining element into a single list and append it to the list containing all permutations
# 6. return all permutations list 


# def permutations(values: list):
#     if len(values) == 1:
#         return [values] 
    
#     allPermutations = []

#     for i in range(len(values)):
#         currentElement = values[i] 
#         remainingElements = values[:i] + values[i+1:]

#         for perm in permutations(remainingElements):
#             allPermutations.append([currentElement] + perm)

#     return allPermutations 




def permutations(integers: list):
    if len(integers) == 1:
        return [integers]
    
    allPermutations = [] 

    for i in range(len(integers)):
        currentElement = integers[i]
        remainingElements = integers[:i] + integers[i+1:]

        for perm in permutations(remainingElements):
            allPermutations += [[currentElement] + perm]

    return allPermutations 


x = ['a','b','c']
print(permutations(x))