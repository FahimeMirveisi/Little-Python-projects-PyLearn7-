
courses_sum = 0
course_num = 0

while True:
    score = input('Enter course score:(enter exit to get average)')
    if score == 'exit':
        break
    score = int(score)
    courses_sum = courses_sum + score
    course_num = course_num +1


average = courses_sum / course_num
print('Average = ',average)
