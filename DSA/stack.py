class Stack:
    def __init__(self):
        self.s = []
    def length(self):
        return len(self.s)
    def push(self, value):
        return self.s.append(value)
    def pop(self):
        return self.s.pop()
stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.s)
print(stk.pop())
print(stk.length())




        
