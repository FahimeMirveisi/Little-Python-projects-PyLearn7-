
n = int(input("Enter number of fibonachi terms that you want to print:"))

n1 = 0
n2 = 1

if n <= 0:
    print("The given number is not valid...Please enter a positive number: ")

elif n == 1 :
    print("Fibonachi sequence is: ")
    print(n1)

elif n == 2:
    print("Fibonachi sequence is: ")
    print(n1)
    print(n2)

else:
    print(n1)
    print(n2)
    for i in range(2, n):
        fibo = n1 + n2
        n1 = n2
        n2 = fibo
        print(fibo)