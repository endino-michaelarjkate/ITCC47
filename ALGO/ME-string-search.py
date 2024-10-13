phrase = "He almost lost his thermostat in the lab."
word = "most"

# def countString(long,short):
    # occurences = 0
    # i = 0
    # while i < len(long):
    #     j = 0
    #     while j < len(short):
    #         if long[j] == short[j]:
    #             if j == len(short) - 1:
    #                 occurences += 1
    #             j += 1
    #         else:
    #             break
    #     i += j+1 
    # return occurences
# def countString(long,short):
#     occurences = 0
#     i = 0
#     match_index = 0 
#     while i < len(long):
#         if long[i] == short[match_index]:
#             match_index += 1 
#             if match_index == len(short):
#                 occurences += 1
#                 match_index = 0
#         else:
#             match_index = 0 
#         i += 1
#     return occurences  

# print(countString(phrase,word))



def countString(long, short): 
    count = 0 
    match_index = 0 
    for c in long:
        if c == short[match_index]:
            match_index += 1
            if match_index == len(short):
                count += 1
                match_index = 0 
        else: 
            match_index = 0 
    return count 

print(countString(phrase,word))