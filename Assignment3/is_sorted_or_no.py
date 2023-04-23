# Sort the input array from smallest to largest

list_len = int(input('Enter your list length:'))
num_list = []
for i in range(list_len):
    element = float(input('Enter element of array:'))
    num_list.append(element)

print('not sorted list is: ', num_list)

sort_list = sorted(num_list)
print('sorted list is: ', sort_list)
