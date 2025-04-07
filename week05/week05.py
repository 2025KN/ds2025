class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "Stack in empty!"
        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None    #링크드 리스트의 노드가 삭제될 때 남은 링크도 없애주기
        return popped_node.data

    def peek(self):
        if self.top is None:
            return "Stack in empty!"
        return self.top.data



s1 = Stack()
print(s1.pop())
print(s1.peek())
s1.push("Data structure")
s1.push("Database")
print(s1.pop())
print(s1.peek())


#for i in range(3):
#    print(s1.pop())
