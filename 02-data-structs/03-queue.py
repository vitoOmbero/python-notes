from collections import deque

q = deque([])
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
print(q)

q.popleft()
print(q)

if not q:
    print("queue is empty")
