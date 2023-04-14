import random

words_bank = ["cat", "book", "banana", "USA", "strawberry", "apple", "pen", "Bag", "bus", "Canada", "Iran", "Japan", "France"]
user_mistakes = 0

correct_chars = []
wrong_chars = []

x = random.randint(0, len(words_bank)-1)
word = words_bank[x]
word = word.lower()

while user_mistakes < 6:
    for i in range(len(word)):
        if word[i] in correct_chars:
            print(word[i], end=" ")
        else:
            print("-", end=" ")

    if len(word) == len(correct_chars):
        print("You win 😍😎")
        break

    user_char = input("Please write your guess: ")
    user_char = user_char.lower()
    if len(user_char) == 1:
        if user_char in word:
            correct_chars.append(user_char)
            print("✔")

        else:
            wrong_chars.append(user_char)
            user_mistakes +=1
            print("❌")
    else:
        print("You just can enter one character😊")

if user_mistakes == 6:
    print("Game Over ☠")
    print("Correct answer is: ", word)