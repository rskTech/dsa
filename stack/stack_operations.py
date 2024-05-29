class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, data):
        node = Node(data)
        if self.size == 0:
            self.top = node
            self.size += 1
        else:
            node.next = self.top
            self.top = node
            self.size += 1
            
    def isEmpty(self):
        return self.size == 0
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            cur = self.top
            self.top = cur.next
            self.size -= 1
    
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            cur = self.top
            while cur:
                print(cur.data, end="->")
                cur = cur.next
            print()
            
stack = Stack()
for x in range(10):
    stack.push(x)
print("After Push: ",stack.display())
for y in range(5):
    stack.pop()
print("After POP: ",stack.display())
