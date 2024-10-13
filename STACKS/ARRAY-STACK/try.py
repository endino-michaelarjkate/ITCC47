stack = []

def Try():
    return len(stack) == 0 

print(Try())
stack.append(1)
print(Try())
