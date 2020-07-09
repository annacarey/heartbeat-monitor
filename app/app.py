import sqlite3                              # import sqlite3
from flask import Flask, render_template    # import flask and render_template
from werkzeug.exceptions import abort       # import abort

# Create an app instance
app = Flask(__name__)

# Establish database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get user
def get_user(first_name, last_name):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE first_name = ? AND last_name = ?',
                        (first_name, last_name)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# Endpoint "/"
@app.route("/")
def begin():
    return render_template('home.html')

@app.route("/test")
def test_db():      # Testing the database

    conn = get_db_connection()

    # Get users
    users = conn.execute('SELECT * FROM users').fetchall()

    # Get sensors
    sensors = conn.execute('SELECT * FROM sensors').fetchall()

    # Get heartbeat_readings
    heartbeat_readings = conn.execute('SELECT * FROM heartbeat_readings').fetchall()
    
    conn.close()
    print(heartbeat_readings[0]['user_id'])
    return 'testing database'

# Endpoint "/dashboard"
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('dashboard.html', users=users)


# For __init__ file, wrap in create_app method
# def create_app(test_config=None): 
# For testing, add config information
# if test_config is not None: app.config.update(test_config)
    