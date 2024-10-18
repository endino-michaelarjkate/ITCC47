from Stack import Stack 

def checkOptr(char: str) -> bool:
    """
    Function to check whether a string character is an operator or not. 
    Returns True if it is an operator, False if otherwise.
    """
    listOfOperators = ["^", "*", "/", "+", "-"]
    return char in listOfOperators 

def checkPrecedence(operator: str) -> int:
    """
    Function to check the order of precedence of an operator.
    """
    if operator == "^":
        return 3
    elif operator == "*" or operator == "/":
        return 2 
    elif operator == "+" or operator == "-":
        return 1
    return 0  
    
# def associativity(operator: str) -> int:
#     """
#     Function to check whether operator has right or left associavity.
#     Returns:
#         0 - right associavity
#         1 - left associavity
#     """

#     if operator == "^":
#         return 0
#     return 1 

def checkBracket(operator: str) -> int:
    open = ["(", "{", "["]
    close = [")", "}", "]"] 

    if operator in open:
        return 1 
    elif operator in close:
        return -1
    return 0 

def postfix(exp: str) -> str:
    """
    Function to convert infix expression to postfix expression.
    Arg: str - infix expression 
    Returns: str - postfix expression 
    """ 

    operators = Stack() 
    s = "" 

    for i in range(len(exp)):
        char = exp[i] 

        # if char is an open parentheses 
        if char == "(" or char == "[": 
            operators.push(char) 

        # if char is a close parentheses 
        elif char == ")" or char == "]":
            while checkBracket(operators.getTop()) != 1:
                s += operators.pop() 
            operators.pop()

        # if char is an operand
        elif not checkOptr(char): 
            s += char  

        # if char is ^ and top operator is ^ 
        elif char == "^" and operators.getTop() == "^":
            operators.push(char) 

        # if char is an operator:
        else: 
            # if char has lesser or equal precedence than top operator, pop the stack elements to the string output until first statement is false 
            while not operators.isEmpty() and (checkPrecedence(char) < checkPrecedence(operators.getTop()) or checkPrecedence(char) == checkPrecedence(operators.getTop())):
                s += operators.pop() 

            # if char has greater precedence than top operator, push it to stack 
            operators.push(char) 

    # pop remaining operators from the stack to the string output 
    while not operators.isEmpty():
        s += operators.pop() 

    return s 

if __name__ == "__main__":
    print(postfix("A+B*C-D"))
    print(postfix("a+b*(c^d-e)^(f+g*h)-i"))




       
        
