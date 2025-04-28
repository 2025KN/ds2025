from os import times_result


def pre_order(node): #재귀함수
	if node is None:
		return
	print(node.data, end="->")
	pre_order(node.left)
	pre_order(node.right)


def post_order(node): #재귀함수
	if node is None:
		return
	post_order(node.left)
	post_order(node.right)
	print(node.data,end= "->")


def in_order(node): #재귀함수
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




if __name__ == "__main__":
	numbers = [10,15,8,3,9, 100, 7, 13]
	root = None

	for number in numbers:
		root = insert(root,number)
		
	
	print('BST 구성완료')
	post_order(root)



# #search 함수만들기
# 	find_number = int(input())
# 	current = root
# 	while True:
# 		if find_number == current.data:
# 			print(f"{find_number}을(를) 찾았습니다")
# 			break
# 		elif find_number < current.data:
# 			if current.left is None:
# 				print(f"{find_number}이(가) 존재하지 않습니다")
# 				break
# 			current = current.left
# 		else:
# 			if current.right is None:
# 				print(f"{find_number}이(가) 존재하지 않습니다")
# 				break
# 			current = current.right

