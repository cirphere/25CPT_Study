N = int(input())

class Stack:
    def __init__(self):
        self.value = []
    
    def push(self, item):
        self.value.append(item)

    def pop(self):
        return self.value.pop()

    def size(self):
        return len(self.value)
        
    def empty(self):
        return 1 if len(self.value) == 0 else 0

    def top(self):
        return self.value[-1]

value = Stack()
for _ in range(N):
    line = input().split()
    if line[0] == "push":
        value.push(int(line[1]))
    elif line[0] == "pop":
        print(value.pop())
    elif line[0] == "size":
        print(value.size())
    elif line[0] == "empty":
        print(value.empty())
    elif line[0] == "top":
        print(value.top())
    else:
        value.append(0)


#stack 클래스를 만들고 문제를 풀어야 하는걸까요?
