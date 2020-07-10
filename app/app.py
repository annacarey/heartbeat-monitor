import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import requests
# import serial
# import time

# Create an app instance
app = Flask(__name__)

# Establish database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get user
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user

# Get user's heartrates
def get_user_heartrates(user_id):
    conn = get_db_connection()
    heartrates = conn.execute('SELECT * FROM heartbeat_readings WHERE user_id = ?',
                        (user_id,)).fetchall()
    conn.close()
    return heartrates

# Endpoint "/"
@app.route("/", methods=('GET', 'POST'))
def welcome():
    return render_template('home.html')

# Endpoint "/heart"
# @app.route("/heartrate", methods=('GET', 'POST'))
# def heartrate():
#     if request.method == 'POST':

#     return render_template('home.html')

# Endpoint for dashboard with user id

@app.route('/<int:user_id>')
def user(user_id):
    user = get_user(user_id)
    heartrates = get_user_heartrates(user_id)
    return render_template('dashboard.html', user=user, heartrates=heartrates)

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
    return 'testing database'


# For __init__ file, wrap in create_app method
# def create_app(test_config=None): 
# For testing, add config information
# if test_config is not None: app.config.update(test_config)
    