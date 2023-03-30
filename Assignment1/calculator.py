import math
print("*** Wellcome to calculator ***")

while 1:
    print("+ : sum")
    print("- : sub")
    print("* : multiplication")
    print("/ : division")
    print("sqrt")
    print("factorial")
    print("sin")
    print("cos")
    print("tan")
    print("cot")


    print("Please enter your choice: ")
    op = input()

    if op == '+' or op == '-' or op == '*' or op == '/':
        input_num1 = float(input("Enter number 1: "))
        input_num2 = float(input("Enter number 2: "))
    else:
        input_num = float(input("Enter number: "))


    if op == '+':
        result = input_num1 + input_num2

    elif op == '-':
        result = input_num1 - input_num2

    elif op == '*':
        result = input_num1 * input_num2

    elif op == '/':
        if input_num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = input_num1 / input_num2

    elif op == 'sqrt':
        result = math.sqrt(input_num)

    elif op == 'sin':
        radian_input = math.radians(input_num)
        result = math.sin(radian_input)

    elif op == 'cos':
        radian_input = math.radians(input_num)
        result = math.cos(radian_input)

    elif op == 'tan':
        radian_input = math.radians(input_num)
        result = math.tan(radian_input)

    elif op == 'cot':
        radian_input = math.radians(input_num)
        result = 1 / math.tan(radian_input)

    elif op == 'factorial':
        result = math.factorial(input_num)

    print(result)

    end = input('Do you want to continue? (yes/no)')
    if end == 'no':
        print('Goodbye--- Wish to see you again...')
        break

