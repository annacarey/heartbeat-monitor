# Heartrate Monitoring App with Sensor Simulation

## Goal
Build a web application that displays the latest "heartbeats" from a number of sensors using Flask.

## Instructions
1. Fork and clone the repository
2. ``Cd`` into the ``app`` directory and run ```python init_db.py``` to initialize database and seed data
4. If you need to make changes to anything in the React frontend, ```cd static``` and run ```npm run build``` to update the ``bundle.js`` file
5. ```Cd ..``` and run ```python -m flask run``` to startup your application server
6. Update the server endpoint in the ``Dashboard.js`` and ``sensor.py`` files according to where your server is running
7. In another terminal window run ```python sensor.py sensor_name``` according to what sensor you want to use from your ``init_db.py`` file
8. Go to ``/<int:user_id>`` to view any users that are initialized in the ``init_db.py`` file

## Development Process

### Database
* My SQLite tables are: ``users``, ``sensors``, and ``heartrate_readings``
* ``heartrate_readings`` has a one-to-many relationship with both ``users`` and ``sensors`` (so each ``heartrate_reading`` has ``user_id`` and ``sensor_id`` foreign keys)
* Notes on the ``sensor`` model:
    * The ``sensor`` model has an ``active`` attribute that is a boolean. Currently, I am not using this attribute, but the idea is that if my program was connected to real sensors, I could set the attribute to ``False`` if the program hadn't received a response in a given amount of time
* Notes on the ``user`` model:
    * Creating a ``user`` model wasn't necessary to achieve my goal
    * I did not implement signup or login functionality yet and just have the ``home.html`` template as a placeholder for when I do implement them. I would need to add username/password to my schema.
    * Currently, you can seed new users in the ``init_db.py`` file and access the user's dashboard info by going to the ``/<int> user_id`` route

### Simulating a Sensor
* In order to show my program was connected to a sensor, I decided to simulate a sensor by creating a separate Python program that serves as its own sensor "server"
* I seeded three sensors in my database
* When I run the file in my terminal with a command line argument of the sensor's name, I am simulating a new reading on the specified sensor
* The sensor 'server' in the ``sensor.py`` file takes in the sensor's name and then makes a POST request to my Flask server. The request includes ``bpm``, ``user_id``, and ``sensor_name``. For now, you can set ``bpm`` manually, but eventually that would be actual sensor data. The user's id is also currently just updated manually
* Other considerations:
    * I started to look into websockets for this project, but since I was new to Python/Flask, I chose to use the command line approach to indicate a reading
    * Given what I know of heartrate sensors, I decided to use bpm as the metric, though the question could have been interpreted as having each data entry row be an individual heartbeat
    * I also considered looking into libraries that can connect to Arduino and/or RasberryPi sensor data such as the ``serial`` library

### Flask Setup
* Basic setup for a Flask app with one main Python file, a database, seed file, and three templates
* My client endpoints in Flask are ``/`` and ``/<int:user_id>``
    * ``/`` is the dummy homepage with a login/signup form that is not yet implemented
    * ``/<int:user_id>`` is the user's dashboard that renders the Dashboard React component.
* Other important routes:
    * ``/heartrate``, a POST route that allows my sensors to post a reading to the database
    * ``/get_heartrate_readings/<int:user_id>`` is used by the frontend to get the user's heartrate readings

### React Setup
* I chose to use React instead of just using the Flask templates so that I could more easily extend my application's frontend and because it was easier for me to make fetch requests on an interval. 
* The Dashboard template connects to a very small React application via a script that is created with Webpack and Babel. 
* One important note is that I am passing the user's id down as a prop to the root component in ``index.js`` which is then passed to the Dashboard component. I needed the user id for my fetch request. I'm interested in thinking through alternatives to make sure the Dashboard component knows about which user's page is currently loading without using React routing. 
* If I extended the frontend, I would connect the React component to the base template instead of the dashboard template
* The Dashboard component uses hooks to set the first name of the current user and their heartrate readings. I used the ``useEffect`` method to make an initial fetch to the Flask server for the user's heartrate info and then set an interval for every five seconds to check the server for an updated reading. Another way to think about it is that my client is polling my server for updates.
* There is a lot of ways I could have shown updated heartrate readings on the client side including web sockets as mentioned above. I could have had the client communicate directly with a sensor. Instead, I chose to have the server communicate with the sensor to both store the sensor data in the database and render the updated data on the frontend with a five second delay (at most).


### Testing
* In the ``tests`` directory, there is an initial setup with ``pytest`` to create an instance of my app for testing. I am new to testing and it's top of my list for skills to develop. Because I was new to Flask/Python, I decided to leave the testing for a later extension.
* In an ideal world, I would set up unit tests for each of my database models to make sure my database is set up properly, for each of my methods in my ``app.py`` file, and for my React component as well.
* Currently there is a testing route in my ``app.py`` to show some of my initial testing process to make sure my database was working properly.

## Contact
If you want to contact me, you can reach out at anna@annajcarey.com.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)