import gtts
import os

words_bank = []


def read_from_file():
    f = open("../Assignment8/translate.txt", "r")

    big_string = f.read()
    temp = big_string.split("\n")

    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i + 1]}
        words_bank.append(my_dict)
    f.close()


def write_to_file(new_w):

    f = open("../Assignment8/translate.txt", "a")
    f.write("\n" + new_w["en"])
    f.write("\n" + new_w["fa"])
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


def translate_persian_to_english():
    user_text = input("Enter your persian text: ")

    user_sentences = user_text.split(".")

    for user_sentence in user_sentences:
        output = ""
        user_words = user_text.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word == word["fa"]:
                    output = output + word["en"] + " "
                    break
            else:
                output = output + user_word + " "

        print(output)

        result = gtts.gTTS(output, lang="en", slow=False)
        result.save("../Assignment8/out_voice.mp3")


def add_new_word():
    eng_w = input("Enter the english word that you want to add to database: ")
    far_w = input("Enter the translate of english word that you want to add to database: ")
    new_w = {"en": eng_w, "fa": far_w}
    words_bank.append(new_w)
    write_to_file(new_w)


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
        translate_persian_to_english()
    elif choice == 3:
        add_new_word()
    elif choice == 4:
        exit(0)
