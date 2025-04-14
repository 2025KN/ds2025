class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None   #앞을 가리키는
        self.rear = None    #뒤를 가리키는
        self.size = 0

    def enqueue(self, data):
        self.size = self.size +1
        node = Node(data)
        if self.rear is None:   #rear = None일때 (처음 만들 때)
            self.front = node   #처음 만들 떈, front, rear 같음
            self.rear = node
        else:                       #처음 만든 게 아닐 땐
            self.rear.link = node   #처음 만들어진 node의 링크를 이번에 새로 만든 node로 연결
            self.rear = node        #rear가 이번에 새로 만든 node를 가리키도록. #move

    def dequeue(self):
        if self.front is None: #큐가 비어있을 때
            raise IndexError("Queue is empty")
        self.size = self.size - 1
        temp = self.front
        self.front = self.front.link    #move #큐에 node가 하나뿐일 때, front를 None으로 바꿈
        temp.link = None                #남아있는 link 삭제
        if self.front is None:
            self.rear = None
        return temp.data





q = Queue()
q.enqueue("Data structure")
q.enqueue("Database")

print(q.size, q.front.data, q.rear.data)

print(q.dequeue())
print(q.size, q.front.data, q.rear.data)

print(q.dequeue())
print(q.size, q.front, q.rear)