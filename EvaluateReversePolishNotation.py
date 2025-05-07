class Stack:
    def __init__(self):
        self.stack = []
         
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

def evalRPN(tokens):
    if len(tokens) == 1: return int(tokens[0])
    
    stk = Stack()
    
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }
    
    for val in tokens:
        if val != '+' and val != '-' and val != '*' and val != '/':
            stk.push(val)
        else:
            secondOperand = int(stk.pop())
            firstOperand = int(stk.pop())
            
            stk.push(ops[val](firstOperand, secondOperand))
                
    print(stk.top())
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

evalRPN(tokens)