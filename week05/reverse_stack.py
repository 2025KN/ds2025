abc = "super"

print(abc[::-1])    #파이썬 슬라이싱 기술을 이용함, 슬라이싱: 문자열[시작:끝:스텝]
                    #문자열의 끝에서 시작해서 한 글자씩 뒤로(-1) 이동하면서 전체 문자열을 거꾸로 나열

print(abc[::2])     #2칸씩



print(''.join(reversed(abc)))   #join()은 리스트나 튜플 등 여러 개의 문자열을 하나의 문자열로 합치는 메서드입니다.
                                # ""는 빈 문자열이니까, 사이에 아무 구분자 없이 붙이라는 뜻입니다.
            #내장 함수 reversed()는 **이터러블(반복 가능한 객체)**을 뒤에서부터 순회할 수 있는 **이터레이터(iterator)**를 반환합니다.
            #문자열 "super"을 넣으면, 내부적으로 'r', 'e', 'p', 'u', 's' 순서로 하나씩 뽑아낼 수 있는 객체가 생깁니다.



def reverse_string(a_string):   #문자열을 매개변수로 받는다
    stack = list()              #stack이라는 이름의 리스트 만들기
    string = ""                 #string이라는 이름의 문자열을 받을 변수 선언
    for letter in a_string:     #매개변수로 받은 문자열을 글자 하나씩 떼어서 stack에 저장
        stack.append(letter)
    for letter in a_string:     #매개변수로 받은 문자열의 길이만큼 반복
        string +=stack.pop()    #stack에 저장한 문자열을 끝부터 떼어내어 string 변수에 저장  (스택 구조)
    return string               #모든 작업이 끝나면 string 변수를 반환한다.

print(reverse_string("bieber"))     #문자열의 가장 뒷 문자부터 이어붙였으므로, 문자열이 뒤집힌다.