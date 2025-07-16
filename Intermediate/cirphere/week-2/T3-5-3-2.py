from collections import deque
n = int(input())

# Please write your code here.
class deQueue:
    def __init__(self):
        self.value = deque()

    def push_front(self, item):
        self.value.appendleft(item)
    
    def push_back(self, item):
        self.value.append(item)

    def pop_front(self):
        print(self.value.popleft())

    def pop_back(self):
        print(self.value.pop())

    def size(self):
        print(len(self.value))

    def empty(self):
        print(1 if len(self.value) == 0 else 0)
    
    def front(self):
        print(self.value[0])

    def back(self):
        print(self.value[-1])

deq = deQueue()
for _ in range(n):
    line = input().split()
    if line[0] == "push_front":
        deq.push_front(line[1])
    elif line[0] == "push_back":
        deq.push_back(line[1])
    elif line[0] == "pop_front":
        deq.pop_front()
    elif line[0] == "pop_back":
        deq.pop_back()
    elif line[0] == "size":
       deq.size()
    elif line[0] == "empty":
       deq.empty()
    elif line[0] == "front":
        deq.front()
    elif line[0] == "back":
        deq.back()
    else:
        A.append(0)
