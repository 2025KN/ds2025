cities = ['Incheon','Seoul', 'Incheon', 'Incheon', 'Gwangju'] #리스트는 중복이 가능
cities = set(cities)    #set을 통해 중복이 사라지고, 익셔너리와 같이 중괄호에 묶여 킷값처럼 나옴
cities.add('Incheon')   #중복값이라 set에 들어가지 않음
cities.add('Suwon')     #새로운 값이라 들어감

print(cities)   #실행할 때마다 순서가 바뀜