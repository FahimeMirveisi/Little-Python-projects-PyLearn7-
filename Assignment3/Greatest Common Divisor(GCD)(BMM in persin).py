
"""
Linear Quest
Algorithm



    1. Initialize GCD = 1
    2. Run a loop in the iteration of (i) between [1, min(num1+1, num2+1)]
    3. Note down the highest number that divides both num1 & num2
    4. If i satisfies (num1 % i == 0 and num2 % i == 0) then new value of GCD is i
    5. Print value of GCD


"""

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

gcd = 1

for i in range(1, min(num1+1, num2+1)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i


print('GCD of', num1, 'and', num2, 'is', gcd)
