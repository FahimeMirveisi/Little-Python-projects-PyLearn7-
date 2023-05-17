
def rhombus_maker(n):
    odds = []
    for m in range(2*n):
        if m % 2 != 0:
            odds.append(m)
    s = n
    for i in range(n):
        print(s * ' ', end='')
        for j in range(odds[i]):

            print('*', end='')
        print()
        s -= 1

    odds.pop()
    odds = list(reversed(odds))
    odds.append(0)

    for i in range(n):
        print((i+2) * ' ', end='')
        for j in range(odds[i]):
            print('*', end='')
        print()


n = int(input('Enter number of rows:'))
rhombus_maker(n)
