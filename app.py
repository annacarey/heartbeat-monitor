import sqlite3
from flask import Flask           # import flask

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
# def hello():                      # call method hello
#     return "Hello World!"         # which returns "hello world"

def test_db():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    print(users[1]['first_name'])
    return 'hi'

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)           # run the flask app in debug mode

    