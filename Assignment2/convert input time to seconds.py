
str_time = input("Enter your input time:")

# h = hour, m = minute, s = second
h, m, s = str_time.split(':')
h = int(h)
m = int(m)
s = int(s)

sec_time = h*3600 + m*60 + s
print(sec_time)

