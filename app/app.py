import sqlite3                    # import sqlite3
from flask import Flask           # import flask

# Establish database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create an app instance
app = Flask(__name__)

# Endpoint "/"
@app.route("/")

def test_db():      # Testing the database
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    sensors = conn.execute('SELECT * FROM sensors').fetchall()
    heartbeat_readings = conn.execute('SELECT * FROM heartbeat_readings').fetchall()
    conn.close()
    print(heartbeat_readings[0]["user"])
    return 'hi'

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)           # run the flask app in debug mode