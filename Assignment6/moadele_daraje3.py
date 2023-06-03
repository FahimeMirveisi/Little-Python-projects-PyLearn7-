import math

print("Hi welcome\nformat of Grade 3 equation is like this: \nax3 + bx2 + cx + d = 0")
print("Please enter a,b,c and d parameters")


def cubic_equation(a, b, c, d):

    p = b - (a ** 2)/3
    q = (2 * a ** 3) / 27 - a*b / 3 + c

    delta = q**2 / 4 + p**3 / 27

    if delta > 0:
        x = (-q/2 + math.sqrt(delta)) ** (1/3) + (-q/2 - math.sqrt(delta)) ** (1/3) - a/3
        return x

    elif delta == 0:
        x1 = -2 * (q/2) ** (1/3) - (a/3)
        x2 = x3 = (q/2) ** (1/3) - (a/3)
        return [x1, x2, x3]

    else:
        x1 = (2/math.sqrt(3)) * math.sqrt(-p) * math.sin(
            (1/3) * math.sinh((3 * math.sqrt(3) * q) / (2 * math.sqrt(-p) ** 3))) - (a/3)

        x2 = (2 / math.sqrt(3)) * math.sqrt(-p) * math.sin(
            (1 / 3) * math.sinh((3 * math.sqrt(3) * q) / (2 * math.sqrt(-p) ** 3)) + (math.pi / 3)) - (a / 3)

        x3 = (2 / math.sqrt(3)) * math.sqrt(-p) * math.sin(
            (1 / 3) * math.sinh((3 * math.sqrt(3) * q) / (2 * math.sqrt(-p) ** 3)) + (math.pi / 6)) - (a / 3)

        return [x1, x2, x3]


a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
d = float(input("Enter d:"))

if cubic_equation(a, b, c, d) is list:
    x1, x2, x3 = cubic_equation(a, b, c, d)
    print("answers is: ", x1, x2, x3)
else:
    x = cubic_equation(a, b, c, d)
    print("answer is: ", x)








