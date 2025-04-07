def is_valid_parentheses(expression : str) -> bool: #type hint, (매개타입) -> 리턴타입
    stack = list()
    brackets = {']':'[', '}':'{', ')': '('}

    for letter in expression:       #문자열에서 글자 하나씩 가져와서 검사
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack        #stack에 값이 있는지 확인


print(is_valid_parentheses("[({1+2)]}"))
print(is_valid_parentheses("[({1+2})]"))

print(is_valid_parentheses("(1+2))"))
print(is_valid_parentheses("(1+2)"))
print(is_valid_parentheses("((3*2)/2)"))
print(is_valid_parentheses("((3*2/2)"))
