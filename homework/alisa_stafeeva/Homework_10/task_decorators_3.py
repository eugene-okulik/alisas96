def select_operation(func):

    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first * second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'

        result = func(first, second, operation)
        return result

    return wrapper
        

@select_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '*':
        return first * second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second

first, second = int(input('Enter first number:')), int(input('Enter second number:'))
print(calc(first, second))
