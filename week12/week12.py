from collections import deque

d = deque([91,17,33])

d.append(12)
d.appendleft(100)
d.append(-14)   #enqueue

for _ in range(len(d)):
    print(d.popleft())  #dequeue
