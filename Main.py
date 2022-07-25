import os
class Stack:
    def __init__(self, size,top):
        self.items = []
        self.size = size
        self.top=-1
        
    def is_empty(self):
        # Write code here
        return self.top == -1
    def is_full(self):
        # Write code here
        return self.top == self.size
    def push(self, data):
        if not self.is_full():
            # Write code here
        else:
            self.top += 1
    def pop(self):
        if not self.is_empty():
            # Write code here
        else:
            self.top -= 1
    def status(self):
        # Write code here
        for i in range (self.top+1):
# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
