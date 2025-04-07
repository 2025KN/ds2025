#print(1+2))

def is_valid_parentheses(expression : str) -> bool: #type hint, (매개타입) -> 리턴타입
    stack = list()
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter ==")":
            if len(stack) ==0:
                return False        #(1+2))
            else:
                stack.pop()

    return len(stack) == 0          #(1+2), ((3*2)/2), ((3*2/2)


print(is_valid_parentheses("(1+2))"))
print(is_valid_parentheses("(1+2)"))
print(is_valid_parentheses("((3*2)/2)"))
print(is_valid_parentheses("((3*2/2)"))
