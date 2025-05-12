from os import times_result


def pre_order(node):  # 재귀함수
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):  # 재귀함수
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end="->")


def in_order(node):  # 재귀함수
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)


class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def insert(root, value):
    node = TreeNode()
    node.data = value

    if root is None:
        return node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = node
                break
            else:
                current = current.left  # 이동
        else:
            if current.right is None:
                current.right = node
                break
            else:
                current = current.right  # 이동
    return root

def search(find_number):
    #search 함수만들기
	current = root
	while True:
		if find_number == current.data:
			return True
		elif find_number < current.data:
			if current.left is None:
				return False
			current = current.left
		else:
			if current.right is None:
				return False
			current = current.right


def delete(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else: #같은 경우, 삭제할 노드를 찾음.
        # leaf 노드거나 자식이 1개인 경우의 노드를 삭제
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        #자식이 2개인 경우
        #오른쪽에서 가장 작은 것 또는 , 왼쪽에서 가장 큰 것 올려주기
        max_smaller_node = node.left
        # min_larger_node = node.right
        # while min_larger_node.left: #왼쪽(작은) 노드가 존재하면.
        #     min_larger_node = min_larger_node.left  # move
        # node.data = min_larger_node.data
        # node.right = delete(node.right, min_larger_node.data)


        while max_smaller_node.left: #왼쪽(작은) 노드가 존재하면.
            max_smaller_node = max_smaller_node.right  # move
        node.data = max_smaller_node.data
        node.left = delete(node.left, max_smaller_node.data)



    return node


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 100, 7, 13]
    root = None

    for number in numbers:
        root = insert(root, number)

    print('BST 구성완료')
    post_order(root) #root가 항상 마지막에 처리
    print()
    in_order(root) #L P R
    print()
    pre_order(root) #root가 항상 처음에
    print()

    # find_number = int(input("찾는 수는?"))
    # if search(find_number):
    #     print(f"{find_number}을(를) 찾았습니다.")
    # else:
    #     print(f"{find_number}을(를) 찾지 못함")

    delete_number = int(input("제거할 숫자는? "))
    root = delete(root, delete_number)
    post_order(root)  # root가 항상 마지막에 처리
    print()
    in_order(root)  # L P R
    print()
    pre_order(root)  # root가 항상 처음에
    print()