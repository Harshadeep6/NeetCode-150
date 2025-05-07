import bisect

class MinStack:

    def __init__(self):
        self.stack = []
        self.ascStack = []

    def push(self, val):
        self.stack.append(val)
        bisect.insort(self.ascStack, val)

    def pop(self):
        if self.stack:
            self.ascStack.remove(self.stack[-1])
            self.stack = self.stack[:-1]
        
    def top(self):
        if self.stack: return self.stack[-1]
        
    def getMin(self):
        return self.ascStack[0]
                

stk = MinStack()

stk.push(10)
stk.push(5)
stk.push(20)

print(stk.pop())
print(stk.stack)
print(stk.ascStack)