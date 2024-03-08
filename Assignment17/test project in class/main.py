
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def test():
    print("salam salam")

def say_Hello():
    my_window.textEdit.setText("Hello QT")

my_app = QApplication([])

loader = QUiLoader()
my_window = loader.load("mainwindow.ui")

print(type(my_window))
my_window.show()

my_window.Fahime.clicked.connect(test)
my_window.Fateme.clicked.connect(say_Hello)

my_app.exec()