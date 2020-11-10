import sqlite3

# Creando archivo donde se almacenara la BD
connection = sqlite3.connect('database.db')

with open('schema.txt', "r", encoding="utf-8") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
