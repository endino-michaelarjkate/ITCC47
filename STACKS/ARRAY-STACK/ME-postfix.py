def precedence(operator: str) -> int:
    if operator == "^":
        return 3
    elif operator == "/" or operator == "*":
        return 2 
    elif operator == "+" or operator == "-":
        return 1 
    return 0 

def postfix(expression: str): 
    stack = [] 
    s = ""

    for i in range(len(expression)):
        char = expression[i]

        # if the character is an operand
        if (char >= "A" and char <= "Z") or (char >= "a" and char <= "z") or (char >= "0" and char <= "9"):
            s += char 

        elif char == "(":
            stack += char 

        elif char == ")":
            while stack[-1] != "(":
                s += stack.pop() 
            stack.pop() 

        # handles right associavity of ^ 
        elif char == "^" and stack[-1] == "^":
            stack += char
        
        # if the character is an operator 
        else:
            # if top element has greater or equal precedence than char 
            while stack and ((precedence(char) < precedence(stack[-1])) or (precedence(char) == precedence(stack[-1]))):
                s += stack.pop()  

            # if stack is empty or top element has lesser precedence than char
            stack += char 

    # pops remaining elements from the stack 
    while stack:
        s += stack.pop() 

    return s 


print(postfix("A+B*C-D"))
print(postfix("a+b*(c^d-e)^(f+g*h)-i"))



