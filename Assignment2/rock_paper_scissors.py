import random

user_score = 0
computer_score = 0

for i in range(5):
    rand_num = random.randint(1, 3)

    if rand_num == 1:
        computer_choice = "rock"
    elif rand_num == 2:
        computer_choice = "paper"
    elif rand_num == 3:
        computer_choice = "scissors"

    user_choice = input("Hey you 👀 Enter your choice...(rock, paper, scissors)")


    print("💻:", computer_choice)
    print("🙂:", user_choice)
    print('-----------------')





    if computer_choice == user_choice:
        print("Equal... scores remain without change")

    elif computer_choice == "rock" and user_choice == "paper":
        user_score = user_score +1

    elif computer_choice == "paper" and user_choice == "rock":
        computer_score = computer_score +1

    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score = computer_score +1

    elif computer_choice == "scissors" and user_choice == "rock":
        user_score = user_score +1

    elif computer_choice == "paper" and user_choice == "scissors":
        user_score = user_score +1

    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score = computer_score +1

    print("💻 score:", computer_score)
    print("🙂 score:", user_score)

print('******************************************')
if computer_score > user_score :
    print("Game over 😕")

if computer_score == user_score:
    print("Your scores are equal 🙄")
else:
    print("You win 😍")




