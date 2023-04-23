
input_num = int(input('enter your number to check: '))

i = 1

while input_num > 1:
    if input_num % i == 0:
        input_num /= i

    else:
        break
    i += 1

if 1 == input_num:
    print('yes')
else:
    print('No')
