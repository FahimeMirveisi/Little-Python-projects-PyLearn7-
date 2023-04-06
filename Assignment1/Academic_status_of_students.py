
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
Grades = []
for i in range(3):
    print("Enter grade",i+1,": ")
    grade = float(input())
    Grades.append(grade)

print(Grades)

avg = (Grades[0] + Grades[1] + Grades[2]) / 3

if avg >= 17:
    print('Great')
elif 17 > avg >= 12:
    print('Normal')
else:
    print('Fail')

