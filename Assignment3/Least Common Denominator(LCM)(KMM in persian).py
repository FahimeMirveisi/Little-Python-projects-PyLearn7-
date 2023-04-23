
"""
Linear Quest
Algorithm

    For a input num1 and num2. This method uses two following observations –

    1. LCM of two numbers will at least be equal or greater than max(num1, num2)
    2. Largest possibility of LCM will be num1 * num2

When iterating in (i) We can linearly find an (i) that is divisible by both num1 & num2

"""


num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

# Define default value for lcm
lcm = 'lcm is not defined'
for i in range(max(num1, num2), (num1 * num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break

print('LCM of', num1, 'and', num2, 'is', lcm)
