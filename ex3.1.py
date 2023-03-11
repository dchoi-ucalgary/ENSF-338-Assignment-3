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
    if is_balanced(expr):
        s = Stack()
        for token in tokenize(expr):
            if token == '(':
                s.push(token)
            if token == ')':
                b = s.pop()
                a = s.pop()
                op = s.pop()
                s.pop()
                if op == '+':
                    s.push(a + b)
                elif op == '-':
                    s.push(a - b)
                elif op == '*':
                    s.push(a * b)
                elif op == '/':
                    s.push(a / b)
            
            if token in ['+', '-', '*', '/']:
                s.push(token)
            if token in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                s.push(int(token))

        while (len(s.items) > 3):
            s.pop()
            b = s.pop()
            a = s.pop()
            op = s.pop()
            if op == '*':
                s.push(a * b)
            elif op == '/':
                s.push(a // b)
            elif op == '+':
                s.push(a + b)
            elif op == '-':
                s.push(a - b)

        return s.pop()


if __name__ == '__main__':
    expr = sys.argv[1]
    if is_balanced(expr):
        result = evaluate(expr)
        print(result)
    else:
        print('Expression is not balanced')
        