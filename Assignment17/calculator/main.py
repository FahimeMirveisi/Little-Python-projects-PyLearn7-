import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


sign = ""

def sum():
    global a
    global sign
    sign = "+"
    a = float(main_window.txt_box.text())
    main_window.txt_box.setText("")

def sub():
    global a
    global sign
    sign = "-"
    a = float(main_window.txt_box.text())
    main_window.txt_box.setText("")


def mul():
    global a
    global sign
    sign = "*"
    a = float(main_window.txt_box.text())
    main_window.txt_box.setText("")

def div():
    global a
    global sign
    sign = "/"
    a = float(main_window.txt_box.text())
    main_window.txt_box.setText("")

def num(x):
    old_number = main_window.txt_box.text()
    new_number = old_number + x
    main_window.txt_box.setText(new_number)


def clear():
    main_window.txt_box.setText("")


def result():
    global c
    b =float(main_window.txt_box.text())

    #if sign in globals():
    if sign == "+":
        c = a + b
    elif sign == "-":
        c = a - b
    elif sign == "*":
        c = a * b
    elif sign == "/":
        c = a / b
    #else:
    main_window.txt_box.setText(str(c))

app = QApplication([])


loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

# calculation buttons
main_window.btn_sum.clicked.connect(sum)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)

#result button
main_window.btn_result.clicked.connect(result)

#numbers buttons
main_window.btn_num_0.clicked.connect(partial(num, "0"))
main_window.btn_num_1.clicked.connect(partial(num, "1"))
main_window.btn_num_2.clicked.connect(partial(num, "2"))
main_window.btn_num_3.clicked.connect(partial(num, "3"))
main_window.btn_num_4.clicked.connect(partial(num, "4"))
main_window.btn_num_5.clicked.connect(partial(num, "5"))
main_window.btn_num_6.clicked.connect(partial(num, "6"))
main_window.btn_num_7.clicked.connect(partial(num, "7"))
main_window.btn_num_8.clicked.connect(partial(num, "8"))
main_window.btn_num_9.clicked.connect(partial(num, "9"))

#clear button
main_window.btn_clear.clicked.connect(clear)


app.exec()