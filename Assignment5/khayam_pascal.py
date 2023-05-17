from math import factorial


def khayyam_and_pascal(m):

    for i in range(m):
        for j in range(i+1):
            print(factorial(i) // (factorial(j) * factorial(i-j)), end=" ")

        print()


n = int(input("Enter row number:"))
khayyam_and_pascal(n)
