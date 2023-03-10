import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

def tokenize(expr):
    for p in ['(',')','[',']','{','}']:
        expr = expr.replace(p, f' {p} ')
    return expr.split()

def is_balanced(expr):
    s = Stack()
    for token in tokenize(expr):
        if token in ['(', '[', '{']:
            s.push(token)
        elif token in [')', ']', '}']:
            if s.is_empty():
                return False
            p = s.pop()
            if p == '(' and token != ')':
                return False
            elif p == '[' and token != ']':
                return False
            elif p == '{' and token != '}':
                return False
    if not s.is_empty():
        return False
    return True

def evaluate(expr):
    s = Stack()
    for token in tokenize(expr):
        if token.isdigit():
            s.push(int(token))
        elif token in ['+', '-', '*', '/']:
            if s.is_empty():
                raise ValueError('Invalid expression')
            b = s.pop()
            if s.is_empty():
                raise ValueError('Invalid expression')
            a = s.pop()
            if token == '+':
                s.push(a + b)
            elif token == '-':
                s.push(a - b)
            elif token == '*':
                s.push(a * b)
            elif token == '/':
                s.push(a / b)
        else:
            raise ValueError('Invalid expression')
    if s.is_empty():
        raise ValueError('Invalid expression')
    return s.pop()

if __name__ == '__main__':
    expr = sys.argv[1]
    if is_balanced(expr):
        result = evaluate(expr)
        print(result)
    else:
        print('Expression is not balanced')
        