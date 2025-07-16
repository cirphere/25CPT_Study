from collections import deque
N = int(input())
# Please write your code here.
class Queue:
    def __init__(self):
        self.value = deque()

    def push(self, item):
        self.value.append(item)
    
    def pop(self):
        print(self.value.popleft())

    def size(self):
        print(len(self.value))

    def empty(self):
        print(1 if len(self.value) == 0 else 0)
    
    def front(self):
        print(self.value[0])


q = Queue()
for _ in range(N):
    line = input().split()
    if line[0] == "push":
        q.push(line[1])
    elif line[0] == "pop":
        q.pop()
    elif line[0] == "size":
        q.size()
    elif line[0] == "empty":
        q.empty()
    elif line[0] == "front":
        q.front()
    else:
        A.append(0)
