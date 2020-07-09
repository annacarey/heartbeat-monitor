import sqlite3                              # import sqlite3
from flask import Flask, render_template    # import flask and render_template

# Create an app instance
def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is not None:
        app.config.update(test_config)
    
    # Endpoint "/"
    @app.route("/")
    def test_db():      # Testing the database
        # Establish database connection
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row

        # Get users
        users = conn.execute('SELECT * FROM users').fetchall()

        # Get sensors
        sensors = conn.execute('SELECT * FROM sensors').fetchall()

        # Get heartbeat_readings
        heartbeat_readings = conn.execute('SELECT * FROM heartbeat_readings').fetchall()
        
        conn.close()
        print(heartbeat_readings[0]['user_id'])
        return "hello"
    
    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    return app