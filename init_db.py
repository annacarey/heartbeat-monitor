import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Seed database with two users
cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)",
            ('Anna', 'Carey')
            )

cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)",
            ('Dean', 'Ginsberg')
            )

cur.execute("INSERT INTO sensors (name, active) VALUES (?, ?)",
            ('pulse_sensor', False)
            )

connection.commit()
connection.close()