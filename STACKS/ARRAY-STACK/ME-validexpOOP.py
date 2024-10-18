from Stack import Stack

def isValid(x: str) -> bool:
    stack = Stack() 

    for i in range(len(x)):
        char = x[i] 

        # if char is an opening bracket
        if char in "({[":
            stack.push(char) 
        
        # if char is a closing bracket
        elif char in ")}]":

            # handle cases where closing bracket comes first before an opening bracket
            if stack.isEmpty(): 
                stack.push(char) 

            # check if top element and char are matching brackets
            elif stack.getTop() == "(" and char == ")":
                stack.pop() 
            elif stack.getTop() == "{" and char == "}":
                stack.pop() 
            elif stack.getTop() == "[" and char == "]":
                stack.pop() 

            # if char and top element does not match; to make sure that stack is not empty --> invalid exp 
            else:
                stack.push(char) 

    # check if stack is empty or not
    if stack.isEmpty():
        return True
    return False 
    
if __name__ == "__main__":
    print(isValid("("))
    print(isValid(")("))
    print(isValid("({)}"))
    print(isValid("()"))
    

            