groups = ['HOT','Seventeen', 'Black Pink', 'NJZ']
#reatings = [1,2,4,3, 100]   #두개의 리스트 중에서 더 작은 (여기서는 groups)리스트 갯수만큼 내부 반복
reatings = [1,2,4,3]

groups_rating = list(zip(groups, reatings))   #zip객체(튜플) 생성 후 리스트로 만듬
print(groups_rating)