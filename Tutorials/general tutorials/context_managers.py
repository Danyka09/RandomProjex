with open("books.txt", "w") as file:
    file.write("The Hunger Games\n")
    file.write("Sunbearer Trials\n")
    file.write("Percy Jackson\n")

# we use context managers cause its easier, more readable and closes file always even when error

#do it like this seperated with a comma instead of nesting
with open("books.txt", "w") as input_file, open("catalog.txt", "w") as output_file:
    titles = input_file.read().split("\n")
    titles.sort()
    output_file.write("\n".join(titles))

# using context managers in sql
import sqlite3

titles = [
    (1, "The Hunger Games"),
    (2, "Sunbearer Trials"),
    (3, "Percy Jackson")
]

with sqlite3.connect("books.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXIST books (
        id INTEGER,
        title TEXT
        )
    """)
    for id, title in titles:
        cursor.execute("INSERT INTO books VALUES (?, ?)", (id, title))