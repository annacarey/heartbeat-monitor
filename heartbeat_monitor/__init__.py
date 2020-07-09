import sqlite3                    # import sqlite3
from flask import Flask           # import flask

# Create an app instance
def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)
    
    # Endpoint "/"
    @app.route("/")
    # def get_db_connection():
    #        conn = sqlite3.connect('database.db')
    #         conn.row_factory = sqlite3.Row
    #         return conn
    def test_db():      # Testing the database
        # conn = get_db_connection()
        
        # Establish database connection
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        users = conn.execute('SELECT * FROM users').fetchall()
        sensors = conn.execute('SELECT * FROM sensors').fetchall()
        heartbeat_readings = conn.execute('SELECT * FROM heartbeat_readings').fetchall()
        conn.close()
        print(heartbeat_readings[0]["user_id"])
        return 'hello'

    return app