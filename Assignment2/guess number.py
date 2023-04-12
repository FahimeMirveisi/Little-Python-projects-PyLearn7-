import random

print('Enter range of number that you want computer to choose:')

start_number = int(input('Start_number:'))
end_number = int(input('end_number:'))

computer_number = random.randint(start_number, end_number)
guess_number = 0

while True:
    print('Enter the number between {} and {} that you guess:'.format(start_number, end_number))
    user_number = int(input())
    guess_number = guess_number +1

    if computer_number == user_number:
        print("Bravo... your answer is correct")
        print('💥💥💥 you win 💥💥💥')
        break

    elif computer_number > user_number:
        print('go up (⬆)')


    elif computer_number < user_number:
        print('go down (⬇)')


print("guess_number: ",guess_number)


