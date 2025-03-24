def duplicate_city(cities):
    result_city = []
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city


cities = ['Incheon','Seoul', 'Incheon', 'Incheon', 'Gwangju'] #리스트는 중복이 가능
# cities = set(cities)    #set을 통해 중복이 사라지고, 익셔너리와 같이 중괄호에 묶여 킷값처럼 나옴
# cities.add('Incheon')   #중복값이라 set에 들어가지 않음
# cities.add('Suwon')     #새로운 값이라 들어감
cities.append('Incheon')
cities.append('Seoul')
cities.append('Suwon')
print(cities)             #실행할 때마다 순서가 바뀜
print(set(duplicate_city(cities)))  #set을 붙임으로서 중복값을 반복되지 않게 만들었다.