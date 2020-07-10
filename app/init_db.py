import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Seed database with two users and heartbeats
cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)",
            ('Anna', 'Carey')
            )

cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)",
            ('Dean', 'Ginsberg')
            )

cur.execute("INSERT INTO sensors (name, active) VALUES (?, ?)",
            ('pulse_sensor_1', True)
            )

cur.execute("INSERT INTO sensors (name, active) VALUES (?, ?)",
            ('pulse_sensor_2', True)
            )
        
cur.execute("INSERT INTO sensors (name, active) VALUES (?, ?)",
            ('pulse_sensor_3', True)
            )

cur.execute("INSERT INTO heartbeat_readings (bpm, user_id, sensor_id) VALUES (?, ?, ?)",
            (70, 1, 1)
            )

cur.execute("INSERT INTO heartbeat_readings (bpm, user_id, sensor_id) VALUES (?, ?, ?)",
            (80, 2, 1)
            )

connection.commit()
connection.close()