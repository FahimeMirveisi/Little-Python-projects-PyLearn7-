
import os

def read_from_file():
    global words_bank
    
    f = open("F:\\PyLearn7 Projects\\Little-Python-projects-PyLearn7-\\Assignment8\\translate.txt", "r")
    
    big_string = f.read()
    temp = big_string.split("\n")
    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)
    f.close()


def translate_english_to_persian():
    user_text = input("Enter your english text: ")

    user_words = user_text.split(" ")

    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "

    print(output)


def show_menu():
    print("welcome to my translate")
    print("1- translate english to persian")
    print("2- translate persian to english")
    print("3- add a new word to database")
    print("4- exit")


read_from_file()

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        ...
    elif choice == 3:
        ...
    elif choice == 4:
        exit(0)




