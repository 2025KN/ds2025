def my_zip(l1,l2):
    l3 = list()
    length = 0
    if len(l1) < len(l2):
        length = len(l1)
    else:
        length = len(l2)
    for i in range (length):
        l3.append((l1[i],l2[i]))
    return  l3

groups = ['HOT','Seventeen', 'Black Pink', 'NJZ']
#reatings = [1,2,4,3, 100]   #두개의 리스트 중에서 더 작은 (여기서는 groups)리스트 갯수만큼 내부 반복
reatings = [1,2,4,3]

groups_rating = my_zip(groups, reatings)
print(groups_rating)