sec_time = int(input("Enter your input time:"))

# h = hour, m = minute, s = second
h = int(sec_time/3600)
temp = sec_time%3600

m = int(temp/60)
temp = temp%60

s = temp


if h<=9 :
    h = '0{}:'.format(h)
else:
    h = str(h)

if m<=9 :
    m = '0{}:'.format(m)
else:
    m = str(m)

if s<=9 :
    s = '0{}'.format(s)
else:
    s = str(s)

str_time = h + m + s
print(str_time)