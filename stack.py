
from collections import deque

l = [11,22,33,44,55]
print(l)
l.append(66)
print(l)
l.insert(0, 00)
print(l)
print(l.pop(0))
print(l)
print(l.pop())
print(l)
l.append(0)
print(l)

l3 = deque([100,200,300])
print(l3)
l3.append(400)
print(l3)
print(l3.popleft())#ilk baştan çıkarır
print(l3)