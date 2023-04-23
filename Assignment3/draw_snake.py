
snake_length = int(input('Enter snake length: '))
snake_str = ''
for i in range(snake_length):
    if i%2 == 0:
        snake_str += '*'
    else:
        snake_str += '#'

print(snake_str)