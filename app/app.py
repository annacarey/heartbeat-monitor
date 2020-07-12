import sqlite3
from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from werkzeug.exceptions import abort
import requests
import json

# Create an app instance
app = Flask(__name__)

# Set up dict factory
def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Establish database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
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
# Expose endpoint '/get_heartrate_readings/2' to access info via API call
@app.route('/get_heartrate_readings/<int:user_id>')
def get_user_heartrates(user_id):
    conn = get_db_connection()
    heartrates = conn.execute('SELECT * FROM heartbeat_readings WHERE user_id = ?',
                        (user_id,)).fetchall()
    conn.close()
    return json.dumps({"heartrates": heartrates})   # Returns json object

# Endpoint "/"
@app.route("/", methods=('GET', 'POST'))
def welcome():
    return render_template('home.html')
    
# Endpoint "/heartrate" to get information from the sensor
@app.route("/heartrate", methods=('GET', 'POST'))
def heartrate():
    if request.method == 'POST':

        # Parse the incoming json
        data = request.get_json()
        bpm = data.get('bpm')
        sensor_name = data.get('sensor_name')
        user_id = data.get('user_id')

        # Get sensor id
        conn = get_db_connection()
        sensor_id = conn.execute('SELECT * FROM sensors WHERE name = ?',
                        (sensor_name,)).fetchone()["id"]

        # Add a reading into the database
        cur = conn.cursor()
        cur.execute("INSERT INTO heartbeat_readings (bpm, user_id, sensor_id) VALUES (?, ?, ?)",
            (bpm, user_id, sensor_id)
            )
        conn.commit()
        conn.close()
        return 'Added heartrate to the database'

# Endpoint "/:user_id" to show dashboard
@app.route('/<int:user_id>')
def user(user_id):
    user = get_user(user_id)
    heartrates = get_user_heartrates(user_id)
    print(heartrates)
    return render_template('dashboard.html', user=user, heartrates=heartrates)

# Testing the database connection and schema
@app.route("/test")
def test_db():

    conn = get_db_connection()

    # Get users
    users = conn.execute('SELECT * FROM users').fetchall()

    # Get sensors
    sensors = conn.execute('SELECT * FROM sensors').fetchall()

    # Get heartbeat_readings
    heartbeat_readings = conn.execute('SELECT * FROM heartbeat_readings').fetchall()
    
    conn.close()
    return 'Testing database'


# For __init__ file, wrap in create_app method
# def create_app(test_config=None): 
# For testing, add config information
# if test_config is not None: app.config.update(test_config)
    