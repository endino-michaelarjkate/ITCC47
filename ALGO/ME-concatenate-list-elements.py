def combineStrings(list1,list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result 

l1 = ["m","na","i","ne","jo"]
l2 = ["y", "me", "s", "il", "hn"]
print(combineStrings(l1,l2))