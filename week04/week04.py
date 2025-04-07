class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link



# a = Node("ABC")

#링크드 리스트는 맨 처음 노드를 가리키는 head, 그리고 node는 값을 지닌 data와 다음 노드를 가리키는 link로 이루어져 있다.
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:               #리스트가 비어있다면(새로 생성된 상태??)
            self.head = Node(data)      #head가 가리키는 node를 하나 생성하고 끝(아직 값이 없는 상태)
            return
        current = self.head             #head가 가리키는 node를 current라고 지칭
        while current.link:             #current가 가리키는 link가 있다면
            current = current.link #move current    #그 link를 따라서 마지막 링크까지 가기
        current.link = Node(data)                   #마지막 링크에 해당하는 노드까지 가서 그 노드의 링크값을 새로 생성된 node로 설정 (이 때 새로 생선된 node는 data=data, link=None)

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

    def recerse_list(self):
        #링크드 리스트를 뒤집으려면 필요한 것.
        #node는 다음 node를 가리키고 있음
        #head는 항상 첫번째 node를 가리킴

        #head가 마지막 node를 가리키게 해야 함. (마지막에 해야 할듯)
        #1. 역순의 인덱스로 다시 생성?
        #2. 기존 리스트에서 추가 변수 생성하여 각각 이전 노드를 가리키게 하고, head의 값을 바꾸기

        current = self.head           #head가 가리키는 node
        previous = None               #변수
        while current:                #current가 존재하면                              #다음 node가 있다면
            next = current.link       #next변수에 current가 가리키는 node 대입           #next가 다음 노드를 가리키도록.
            current.link = previous   #current.link에 previous 대입(처음엔 None)        #현재 노드의 link에 이전 노드를 가리키도록.
            previous = current        #previous에 current 대입
            current = next            #current에 head가 가리키던 node 대입
        self.head = previous

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(8))
ll.remove(10)
ll.remove(77)
print(ll)

