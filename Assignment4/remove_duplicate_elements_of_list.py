
list_len = int(input('Enter your list length:'))
num_list = []
for i in range(list_len):
    element = float(input('Enter element of array:'))
    num_list.append(element)

non_duplicate = set(num_list)
print(non_duplicate)
non_duplicate = list(non_duplicate)

print('original list: ', num_list)
print('list without duplicates: ', non_duplicate)
