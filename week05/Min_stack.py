#스택에서 가장 작은 요소를 추적하는 최소 스택.

class MinStack():
    def __init__(self):
        self.main = []
        self.min = []

    def push(self, n):
        if len(self.main) == 0 :            #main 스택이 비어있다면
            self.min.append(n)              #min 스택에 그대로 넣고,  15번라인으로 가서 main에 넣는다.
        elif n <= self.min[-1]:             #들어온 값이 min 스택에 있는 마지막 값보다 작다면
            self.min.append(n)              #그 값을 min 스택에 넣는다.
        else:
            self.min.append(self.min[-1])   #들어온 값이 이미 min 스택에 있는 값보다 크다면, 원래 가지고 있던 값을 min 스택에 한번 더 추가.
        self.main.append(n)

    def pop(self):
        self.min.pop()                      #pop을 할 땐, 항상 main과 min 스택 둘다 하나씩 빼야 한다.
        return self.main.pop()

    def get_min(self):
        return self.min[-1]




a = MinStack()
a.push(20)
a.push(10)
a.push(30)

print(a.main)
print(a.min)
print(a.get_min())

a.pop()
print(a.main)
print(a.min)
print(a.get_min())

a.pop()
print(a.main)
print(a.min)
print(a.get_min())

a.pop()
print(a.main)
print(a.min)
