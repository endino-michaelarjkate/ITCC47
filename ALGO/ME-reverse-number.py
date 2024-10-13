# x = 12345
# digit = 0
# reverse = ""
# for i in range(len(str(x))):
#     digit = x % 10 
#     x = x // 10 
#     reverse += str(digit) 

# print(reverse)


# s1 = 'abc'
# s2 = 'xyz'
# azbycx

# def combine(s1,s2):
#     s3 = ''
#     s2 = s2[::-1]
#     i = 0 
#     while i < len(s1):
#         s3 += s1[i]
#         s3 += s2[i]
#         i += 1

#     return s3
# print(combine(s1,s2))


# s1 = 'pyf'
# s2 = 'pynative' 

# def isBalanced(s1,s2):
#     i = 0
#     value = False
#     while i < len(s2):
#         if s2[i] in s1:
#             value = True 
#         elif s2[i] not in s1:
#             value = False
#         i += 1 

#     return value 
# print(isBalanced(s1,s2)) 

# str1 = "Welcome to USA. usa awesome, isn't it?" 
# myStr = "USA"

# def countStr(str1,str2):
#     count = 0 
#     match_index = 0 
#     i = 0
#     while i < len(str1):
#         if str1[i].lower() == str2[match_index].lower():
#             match_index += 1
#             if match_index == len(str2):
#                 count += 1
#                 match_index = 0 
#         else:
#             match_index = 0 
#         i += 1 
#     return count 
# print(countStr(str1,myStr))

str1 = "Apple" 

# def countChar(str):
#     char_dict = dict() 
#     for char in str:
#         count = str.count(char)
#         char_dict[char] = count
#     return char_dict 

# print(countChar(str1))

str1[0] = 'b'
print(str1)


