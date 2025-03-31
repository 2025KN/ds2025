class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link



# a = Node("ABC")

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link #move current
        current.link = Node(data)

    def remove(self, target):
        current = self.head
        if self.head.data == target:
            self.head = self.head.link
            current.link = None
            return
        #current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.link  = current.link
                current.link = None #해당 노드의 남아있는 링크 제거
            previous = current
            current = current.link

    #def is_find(self, target):
    def search(self,target):
        current = self.head
        while current: #bug fix
            if target == current.data:
                return f"{target}을(를) 찾았습니다!"
            else:
                current = current.link
        return f"{target}은(는) 링크드 리스트 안에 존재하지 않습니다."

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            # print(current.data)
            #result = result + str(current.data) + " -> "
            result = result + f"{current.data}  -> "
            current = current.link
        #return "END"
        return result + "END"
         # return "Linked list!"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(8))
ll.remove(10)
ll.remove(77)
print(ll)

