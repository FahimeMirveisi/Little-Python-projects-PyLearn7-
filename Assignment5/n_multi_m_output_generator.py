
def output_plate(n, m):
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('#',end='')
                else:
                    print('*',end='')

            else:
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print('#', end='')
        print()


n = int(input("Enter the n number: "))
m = int(input("Enter the m number: "))

output_plate(n, m)


