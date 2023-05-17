
def multiplication_table(n, m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                if j == 0:
                    print('x', end='   ')
                else:

                    print(j, end='   ')
            else:
                if j == 0:
                    print(i, end='   ')
                else:
                    if i*j <10:
                        print(i*j, end='   ')
                    else:
                        print(i*j, end='  ')
        print()


n = int(input("Enter the n number: "))
m = int(input("Enter the m number: "))

multiplication_table(n, m)

