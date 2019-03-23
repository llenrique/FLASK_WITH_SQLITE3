import sqlite3

connection = sqlite3.connect('dogcare.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS pets (id INTEGER PRIMARY KEY,name text, race text, age int, personality text)"
cursor.execute(create_table)

connection.commit()
connection.close()
