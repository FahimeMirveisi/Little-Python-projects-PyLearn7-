import sqlite3

connection = sqlite3.connect("chinook.db")

my_cursor = connection.cursor()

#for data in my_cursor.execute("SELECT * FROM Customer WHERE country = 'France'"):
#   print(data)

