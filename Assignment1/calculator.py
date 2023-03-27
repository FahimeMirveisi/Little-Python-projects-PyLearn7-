import math
print("*** Wellcome to my calculator ***")

print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sqrt")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")

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
    result = math.sin(input_num)

elif op == 'cos':
    result = math.cos(input_num)

elif op == 'tan':
    result = math.tan(input_num)

elif op == 'cot':
    result = math.cot(input_num)

elif op == 'factorial':
    result = math.factorial(input_num)

print(result)