from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],   #A 0
    [1, 0, 0, 1, 0, 0, 0, 0],   #B 1
    [1, 0, 0, 1, 0, 0, 0, 0],   #C 2
    [0, 1, 1, 0, 1, 1, 1, 0],   #D 3
    [0, 0, 0, 1, 0, 1, 0, 0],   #E 4
    [0, 0, 0, 1, 1, 0, 0, 0],   #F 5
    [0, 0, 0, 1, 0, 0, 0, 1],   #G 6
    [0, 0, 0, 0, 0, 0, 1, 0]    #H 7
]

def dfs(g, i, visited): #재귀함수 또는 스택 사용
    visited[i] = True
    print(chr(ord('A')+i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g,j,visited)

def bfs(g, i, visited): #큐를 사용.
    queue = deque([i]) #전달받은 인수를 가지고 시작.(start point)
    visited[i] = 1     #방문 여부 갱신(start point)
    #while len(queue) != 0:
    while queue:    #queue가 비어있을때 까지.
        i = queue.popleft()
        print(chr(ord('A') + i), end= ' ')
        for j in range(len(graph)):
            #열을 반복시키는 j.
            # 행을 반복하는 i,
            if g[i][j] == 1 and not visited[j]: #연결되어 있고, 방문하지 않은 노드.
                queue.append(j)
                visited[j] = 1


visited_dfs = [False for _ in range(len(graph))] #방문 여부 확인 배열
visited_bfs = [0 for _ in range(len(graph))] #방문 여부 확인 배열

dfs(graph, 7, visited_dfs)
print()

bfs(graph, 4, visited_bfs)