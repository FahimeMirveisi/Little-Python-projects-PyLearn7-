import random

array_len = int(input("Enter length of array: "))

rand_array = random.sample(range(100), array_len)

print("Array without duplicates: ", rand_array)