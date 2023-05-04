on = True


def addition():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a + b)


def subtraction():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a - b)


def multiplication():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a * b)


def division():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a / b)


while on:
    operation = input("Please choose +, -, *, / or q: ")
    if operation == '+':
        addition()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiplication()
    elif operation == '/':
        division()
    elif operation == 'q':
        on = False
    else:
        print("Symbol not recognised")
