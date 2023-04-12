import random

computer_number = random.randint(30, 70)
guess_number = 0

while True:
    user_number = int(input('Enter the number between 30 and 70 that you guess:'))
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


