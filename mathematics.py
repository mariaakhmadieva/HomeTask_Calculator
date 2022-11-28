x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def do_it(operation):
    if operation == '+':
        res = x + y
    elif operation == '-':
        res = x - y
    elif operation == '*':
        res = x * y
    elif operation == '/':
        res = x / y
    else:
        res = print('Incorrect data')
    return res
