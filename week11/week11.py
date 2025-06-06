class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def print(self):
        for r in range(self.size):
            for c in range(self.size):
                print(self.graph[r][c], end=' ')
            print()

    def print_graph(self, n):
        for r in range(n):
            for c in range(n):
                print(self.graph[r][c], end=' ')
            print()


G1 = Graph(4) #vertex의 개수
G2 = Graph(4)


# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("G1 무방향 그래프")
for r in range(G1.size):
    for c in range(G1.size):
        print(G1.graph[r][c], end=' ')
    print()


G1.print()

# 0 == A, 1 == B, 2 == C, 3 == D
G2.graph[0][1] = 1; G2.graph[0][2] = 1
G2.graph[3][0] = 1; G2.graph[3][2] = 1

print("G3 방향 그래프")
for r in range(G2.size):
    for c in range(G2.size):
        print(G2.graph[r][c], end=' ')
    print()
G2.print()

G_self = Graph(4)

# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print("G1 무방향 그래프")
for r in range(G1.size):
    for c in range(G1.size):
        print(G1.graph[r][c], end=' ')
    print()
