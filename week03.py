#156page
#l1과 l2 리스트 사이에 중복되는 값을 리스트 l3에 넣는 함수
def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    #return list(s1.intersection(s2))
    return list(s1 & s2) # & = 교집합 기호, | = 합집합 기호, - = 차집합 기호


l1 = [45,5,22,31,7,19]
l2 = [22,1,5,2,7,28,27,19,13,41]
print(inters(l1,l2))
