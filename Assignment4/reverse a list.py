
list_len = int(input('Enter your list length:'))
num_list = []
for i in range(list_len):
    element = float(input('Enter element of array:'))
    num_list.append(element)


print('input list: ', num_list)
print('input reverse list: ', num_list[::-1])
