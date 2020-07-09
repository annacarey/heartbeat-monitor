import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)",
            ('Anna', 'Carey')
            )

cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)",
            ('Dean', 'Ginsberg')
            )

connection.commit()
connection.close()