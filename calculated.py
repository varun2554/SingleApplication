def add():
    x = int(input(''))
    y = int(input(''))
    return x+y
def sub():
    x = int(input(''))
    y = int(input(''))
    return x-y
def mul():
    x = int(input(''))
    y = int(input(''))
    return x*y
def calculator():
    x = input('Select above opition: ')
    if x == 'add':
        add()
    elif x == 'sub':
        sub()
    elif x == 'mul':
        mul()
    else:
        'Not Vaild opition'
calculator()


