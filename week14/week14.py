# s, e = input().split()
# print(type(s),type(e))

# inputs = input().split()
# t = []
# for i in inputs :
#     t.append(int (i))
# print(t)
#
# s, e = t
# print(s, e)

def is_prime(n) -> bool: #시간복잡도 O(n)
    if n <=1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

#문자열"3 16"을 ['3', '16'] 변환 후 int형변환 >> 마지막에 언패킹하여 s,e에 저장
s, e = map(int, input().split())
print(s, e)

for i in range(s, e+1):
    if is_prime(i):
        print(i)
