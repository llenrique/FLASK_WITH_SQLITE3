import sqlite3

conn = sqlite3.connect('data.db')

cursor = conn.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert, user)

users = [
    (2, 'jose1', 'asdf'),
    (3, 'llenrique', 'asdf')
]

cursor.executemany(insert, users)

select = "SELECT * FROM users"
for row in cursor.execute(select):
    print(row)

conn.commit()
conn.close()
